import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# ⚠️ YETKİ KAPSAMI - Yorum yapma yetkisi dahildir
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def upload_video():
    try:
        t_json = os.environ.get('TOKEN_JSON')
        if not t_json:
            print("❌ HATA: TOKEN_JSON bulunamadı!")
            return

        token_data = json.loads(t_json)
        token_data['scopes'] = SCOPES 
        creds = Credentials.from_authorized_user_info(token_data, SCOPES)
        
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            
        youtube = build('youtube', 'v3', credentials=creds)
        print("✅ YouTube API bağlantısı kuruldu.")
        
        video_path = "media/videos/final_output.mp4"
        title = "İbrahim Soykan | Maarif Matematik - Yeni Ders"
        description = ""
        tags = []
        first_comment = "" # Yeni eklendi
        
        # metadata.json dosyasından her şeyi okuyoruz
        if os.path.exists('metadata.json'):
            try:
                with open('metadata.json', 'r', encoding='utf-8') as f:
                    m = json.load(f)
                    title = m.get('title', title)
                    description = m.get('description', description)
                    tags = m.get('tags', [])
                    first_comment = m.get('first_comment', "") # Gemini'den gelen yorumu çekiyoruz
                    print(f"📄 Metadata ve Yorum hazır: {title}")
            except Exception as e:
                print(f"⚠️ metadata.json okunamadı: {e}")

        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags,
                'categoryId': '27'
            },
            'status': {
                'privacyStatus': 'unlisted', # Siz hazır olunca public yaparsınız
                'selfDeclaredMadeForKids': False
            }
        }

        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        request = youtube.videos().insert(part='snippet,status', body=body, media_body=media)
        
        response = None
        while response is None:
            status, response = request.next_chunk()
        
        video_id = response.get('id')
        print(f"🎉 BAŞARI! Video ID: {video_id}")

        # --- OTOMATİK İLK YORUM BÖLÜMÜ ---
        if first_comment:
            print("💬 Otomatik ilk yorum yapılıyor...")
            try:
                youtube.commentThreads().insert(
                    part="snippet",
                    body={
                        "snippet": {
                            "videoId": video_id,
                            "topLevelComment": {
                                "snippet": {
                                    "textOriginal": first_comment
                                }
                            }
                        }
                    }
                ).execute()
                print("✅ İlk yorum başarıyla eklendi.")
            except Exception as comment_err:
                print(f"⚠️ Yorum hatası: {comment_err}")

        # Kapak Fotoğrafı Yükleme
        if os.path.exists("s.png"):
            time.sleep(10)
            youtube.thumbnails().set(videoId=video_id, media_body=MediaFileUpload("s.png")).execute()
            print("✅ Kapak fotoğrafı eklendi.")

    except Exception as e:
        print(f"❌ SİSTEM HATASI: {e}")

if __name__ == "__main__":
    upload_video()
