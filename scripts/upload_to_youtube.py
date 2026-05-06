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
# YAML'dan gelen gizlilik ayarını oku, gelmezse 'public' yap
YOUTUBE_PRIVACY = os.environ.get('YOUTUBE_PRIVACY', 'public')

def upload_to_youtube(video_path, title, description, tags, first_comment):
    try:
        t_json = os.environ.get('TOKEN_JSON')
        if not t_json: 
            print("❌ HATA: TOKEN_JSON bulunamadı!")
            return None
        
        token_data = json.loads(t_json)
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
                'privacyStatus': YOUTUBE_PRIVACY, # BURASI GÜNCELLENDİ
                'selfDeclaredMadeForKids': False
            }
        }

        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        response = youtube.videos().insert(part='snippet,status', body=body, media_body=media).execute()
        video_id = response.get('id')
        print(f"✅ YouTube Yüklemesi Başarılı ({YOUTUBE_PRIVACY})! ID: {video_id}")
        
        # --- KAPAK FOTOĞRAFI ---
        if os.path.exists("s.png"):
            print("🖼️ Kapak fotoğrafı (s.png) ekleniyor...")
            time.sleep(5) 
            try:
                youtube.thumbnails().set(
                    videoId=video_id,
                    media_body=MediaFileUpload("s.png")
                ).execute()
                print("✅ Kapak fotoğrafı eklendi.")
            except Exception as thumb_err:
                print(f"⚠️ Kapak yüklenemedi: {thumb_err}")

        # --- İLK YORUM ---
        if first_comment:
            try:
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
                print("✅ İlk yorum eklendi.")
            except: pass
            
        return video_id
    except Exception as e:
        print(f"❌ YouTube Hatası: {e}")
        return None

# --- INSTAGRAM ADIMI (Make.com kullandığımız için burası opsiyoneldir) ---
# ... (Diğer fonksiyonlar aynı kalabilir ancak Make.com kullandığınız için bu kod hata verse de sorun olmaz)

if __name__ == "__main__":
    video_path = "media/videos/final_output.mp4"
    
    if not os.path.exists(video_path):
        print(f"❌ HATA: Video dosyası bulunamadı: {video_path}")
        exit(1)

    if not os.path.exists('metadata.json'):
        print("❌ HATA: metadata.json bulunamadı!")
        exit(1)

    with open('metadata.json', 'r', encoding='utf-8') as f:
        m = json.load(f)
        title = m.get('title', "Maarif Matematik")
        desc = m.get('description', "")
        tags = m.get('tags', [])
        comment = m.get('first_comment', "")

    # YouTube'a yükle
    yt_id = upload_to_youtube(video_path, title, desc, tags, comment)
    
    # Instagram adımı Make.com üzerinden yürüdüğü için buradaki 'file.io' hatalarını görmezden gelebiliriz.
    print("🚀 İşlem tamamlandı. Make.com Instagram paylaşımı için bekleniyor...")
