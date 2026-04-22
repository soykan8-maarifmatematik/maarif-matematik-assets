import os
import json
import time
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# --- AYARLAR ---
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
IG_ACCOUNT_ID = os.environ.get('INSTAGRAM_ACCOUNT_ID')
IG_ACCESS_TOKEN = os.environ.get('INSTAGRAM_ACCESS_TOKEN')

def upload_to_youtube(video_path, title, description, tags, first_comment):
    """YouTube (Shorts veya Uzun) Yükleme Fonksiyonu"""
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
        print(f"✅ YouTube Başarılı! ID: {video_id}")
        
        if first_comment:
            youtube.commentThreads().insert(part="snippet", body={"snippet": {"videoId": video_id, "topLevelComment": {"snippet": {"textOriginal": first_comment}}}}).execute()
            print("✅ YouTube Yorumu Eklendi.")
            
        return video_id
    except Exception as e:
        print(f"❌ YouTube Hatası: {e}")
        return None

def upload_to_instagram(video_url, caption):
    """Instagram Reels Yükleme Fonksiyonu"""
    if not IG_ACCOUNT_ID or not IG_ACCESS_TOKEN:
        print("⚠️ Instagram bilgileri eksik, atlanıyor.")
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
        time.sleep(60) # Instagram uzun işleme süresi ister
        
        publish_url = f"https://graph.facebook.com/v19.0/{IG_ACCOUNT_ID}/media_publish"
        publish_payload = {'creation_id': creation_id, 'access_token': IG_ACCESS_TOKEN}
        requests.post(publish_url, data=publish_payload)
        print(f"✅ Instagram Reels Yayında!")
    except Exception as e:
        print(f"❌ Instagram Hatası: {e}")

if __name__ == "__main__":
    video_path = "media/videos/final_output.mp4"
    
    # Metadata Oku
    with open('metadata.json', 'r', encoding='utf-8') as f:
        m = json.load(f)
        title = m.get('title', "Maarif Matematik")
        desc = m.get('description', "")
        tags = m.get('tags', [])
        comment = m.get('first_comment', "")

    # 1. YouTube'a Yükle (Her zaman çalışır)
    yt_id = upload_to_youtube(video_path, title, desc, tags, comment)
    
    # 2. Süre Kontrolü (Sadece Shorts/Reels ise Instagram'a git)
    # 90 saniyeden uzun videolar Instagram API tarafından reddedilir.
    try:
        import subprocess
        # Video süresini saniye cinsinden alıyoruz
        cmd = f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {video_path}"
        duration = float(subprocess.check_output(cmd, shell=True))
        
        if duration < 90:
            print(f"🎬 Video süresi {duration:.2f}sn. Instagram'a gönderiliyor...")
            with open(video_path, 'rb') as f:
                up_r = requests.post('https://file.io', files={'file': f}, data={'expires': '1h'})
                temp_url = up_r.json().get('link')
                if temp_url:
                    ig_caption = f"{title}\n\n{desc}\n\n" + " ".join(tags)
                    upload_to_instagram(temp_url, ig_caption)
        else:
            print(f"📏 Video süresi {duration:.2f}sn (90sn üzeri). Instagram adımı atlandı.")
            
    except Exception as e:
        print(f"⚠️ Instagram kontrolünde hata: {e}")
