import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# ⚠️ YETKİ KAPSAMI
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def upload_video():
    try:
        # 1. GitHub Secrets Verilerini Çek
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
        print("✅ YouTube bağlantısı kuruldu.")
        
        # 2. Varsayılan Bilgiler
        video_path = "media/videos/final_output.mp4"
        title = "Maarif Matematik - Yeni Ders"
        description = "Mantık odaklı matematik anlatımı."
        tags = ["matematik", "maarif matematik", "eğitim"]
        
        # 3. Metadata Okuma (Dinamik Başlık ve Açıklama)
        if os.path.exists('metadata.json'):
            try:
                with open('metadata.json', 'r', encoding='utf-8') as f:
                    m = json.load(f)
                    title = m.get('title', title)
                    description = m.get('description', description)
                    tags = m.get('tags', tags)
                    print(f"📄 Dinamik Başlık Alındı: {title}")
            except Exception as e:
                print(f"⚠️ metadata.json okuma hatası: {e}")

        # 4. Yükleme Ayarları (GİZLİLİK: UNLISTED)
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags,
                'categoryId': '27' # Eğitim Kategorisi
            },
            'status': {
                'privacyStatus': 'unlisted',  # ✅ ARTIK LİSTE DIŞI YÜKLENECEK
                'selfDeclaredMadeForKids': False
            }
        }

        print(f"🚀 Video yükleniyor (Gizlilik: Liste Dışı)...")
        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        request = youtube.videos().insert(part='snippet,status', body=body, media_body=media)
        response = request.execute()
        
        video_id = response.get('id')
        print(f"🎉 BAŞARI! Video ID: {video_id}")

        # 5. Kapak Fotoğrafı (s.png)
        if os.path.exists("s.png"):
            time.sleep(5)
            youtube.thumbnails().set(
                videoId=video_id,
                media_body=MediaFileUpload("s.png")
            ).execute()
            print("✅ Kapak fotoğrafı eklendi!")

    except Exception as e:
        print(f"❌ KRİTİK HATA: {e}")

if __name__ == "__main__":
    upload_video()
