import os
import json
import time
import requests
import subprocess
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# --- AYARLAR ---
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
IG_ACCOUNT_ID = os.environ.get('INSTAGRAM_ACCOUNT_ID')
IG_ACCESS_TOKEN = os.environ.get('INSTAGRAM_ACCESS_TOKEN')

def upload_to_youtube(video_path, title, description, tags, first_comment):
    """
    YouTube Yükleme Fonksiyonu: 
    Video dikey/yatay veya kısa/uzun fark etmeksizin HER ZAMAN çalışır.
    """
    try:
        t_json = os.environ.get('TOKEN_JSON')
        if not t_json: return None
        
        token_data = json.loads(t_json)
        token_data['scopes'] = SCOPES 
        creds = Credentials.from_authorized_user_info(token_data, SCOPES)
        
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            
        youtube = build('youtube', 'v3', credentials=creds)
        
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags,
                'categoryId': '27'
            },
            'status': {
                'privacyStatus': 'public',
                'selfDeclaredMadeForKids': False
            }
        }

        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        response = youtube.videos().insert(part='snippet,status', body=body, media_body=media).execute()
        video_id = response.get('id')
        print(f"✅ YouTube Yüklemesi Başarılı! ID: {video_id}")
        
        # --- KAPAK FOTOĞRAFI (THUMBNAIL) ---
        if os.path.exists("s.png"):
            print("🖼️ Kapak fotoğrafı (s.png) YouTube'a mıhlanıyor...")
            time.sleep(20) 
            try:
                youtube.thumbnails().set(
                    videoId=video_id,
                    media_body=MediaFileUpload("s.png")
                ).execute()
                print("✅ Kapak fotoğrafı başarıyla eklendi.")
            except Exception as thumb_err:
                print(f"⚠️ Kapak yüklenemedi: {thumb_err}")

        # --- İLK YORUM ---
        if first_comment:
            youtube.commentThreads().insert(
                part="snippet",
                body={
                    "snippet": {
                        "videoId": video_id,
                        "topLevelComment": {
                            "snippet": {"textOriginal": first_comment}
                        }
                    }
                }
            ).execute()
            print("✅ İlk yorum YouTube'a eklendi.")
            
        return video_id
    except Exception as e:
        print(f"❌ YouTube Hatası: {e}")
        return None

def upload_to_instagram(video_url, caption):
    """Instagram Reels Yükleme Fonksiyonu: Sadece Shorts videolar için çağrılır."""
    if not IG_ACCOUNT_ID or not IG_ACCESS_TOKEN:
        print("⚠️ Instagram API bilgileri eksik, Instagram adımı atlanıyor.")
        return

    try:
        url = f"https://graph.facebook.com/v19.0/{IG_ACCOUNT_ID}/media"
        payload = {
            'media_type': 'REELS',
            'video_url': video_url,
            'caption': caption,
            'access_token': IG_ACCESS_TOKEN
        }
        r = requests.post(url, data=payload)
        creation_id = r.json().get('id')
        
        if not creation_id:
            print(f"❌ Instagram Medya Hatası: {r.text}")
            return

        print("⏳ Instagram videosu işleniyor (60sn bekleniyor)...")
        time.sleep(60) 
        
        publish_url = f"https://graph.facebook.com/v19.0/{IG_ACCOUNT_ID}/media_publish"
        publish_payload = {'creation_id': creation_id, 'access_token': IG_ACCESS_TOKEN}
        requests.post(publish_url, data=publish_payload)
        print(f"✅ Instagram Reels yayına girdi!")
    except Exception as e:
        print(f"❌ Instagram Hatası: {e}")

if __name__ == "__main__":
    video_path = "media/videos/final_output.mp4"
    
    if not os.path.exists('metadata.json'):
        print("❌ HATA: metadata.json dosyası bulunamadı!")
        exit(1)

    with open('metadata.json', 'r', encoding='utf-8') as f:
        m = json.load(f)
        title = m.get('title', "Maarif Matematik")
        desc = m.get('description', "")
        tags = m.get('tags', [])
        comment = m.get('first_comment', "")

    # 1. ADIM: YouTube'a Yükle (VİDEO NE OLURSA OLSUN YÜKLENİR)
    yt_id = upload_to_youtube(video_path, title, desc, tags, comment)
    
    # 2. ADIM: Süre ve Platform Kontrolü
    try:
        cmd = f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {video_path}"
        duration = float(subprocess.check_output(cmd, shell=True))
        
        # Eğer video 90 saniyeden kısaysa (Shorts/Reels formatı) Instagram'a da gönder
        if duration < 90:
            print(f"🎬 Shorts algılandı ({duration:.2f}sn). Instagram'a da gönderiliyor...")
            with open(video_path, 'rb') as f:
                # Geçici link oluştur (Instagram API için gerekli)
                up_r = requests.post('https://file.io', files={'file': f}, data={'expires': '1h'})
                temp_url = up_r.json().get('link')
                if temp_url:
                    # Etiketleri Instagram formatına çevir (#etiket)
                    ig_caption = f"{title}\n\n{desc}\n\n" + " ".join(["#"+t.replace(" ","") for t in tags])
                    upload_to_instagram(temp_url, ig_caption)
        else:
            print(f"📏 Normal video algılandı ({duration:.2f}sn). Sadece YouTube'da yayınlandı.")
            
    except Exception as e:
        print(f"⚠️ Instagram/Süre kontrolünde bir pürüz çıktı: {e}")
