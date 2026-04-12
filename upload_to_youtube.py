import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# KRİTİK: Bu liste anahtar.py ile BİREBİR aynı olmalıdır.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def upload_video():
    # 1. Yetki ve Kimlik Bilgilerini Al
    try:
        client_secrets = json.loads(os.environ.get('CLIENT_SECRETS_JSON'))
        token_data = json.loads(os.environ.get('TOKEN_JSON'))
        
        # Token verisinden kimlik nesnesini oluştur
        creds = Credentials.from_authorized_user_info(token_data, SCOPES)
        
        # Eğer token'ın süresi dolmuşsa yenile (invalid_scope hatasını önler)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            
        youtube = build('youtube', 'v3', credentials=creds)
    except Exception as e:
        print(f"HATA: Kimlik doğrulama başarısız: {e}")
        return

    # 2. Varsayılan Metadata Değerleri
    video_title = "Birim Kesirler Mantığı | Maarif Matematik"
    video_description = "Maarif Modeli'ne uygun ders içeriği."
    video_tags = ["matematik", "maarif"]

    # 3. Güncel Başlığı Oku (metadata.json)
    if os.path.exists('metadata.json'):
        try:
            with open('metadata.json', 'r', encoding='utf-8') as f:
                meta = json.load(f)
                # Make.com'dan gelen yapıyı kontrol et
                data = meta.get('metadata', meta)
                video_title = data.get('title', video_title)
                video_description = data.get('description', video_description)
                video_tags = data.get('tags', video_tags)
                print(f"✅ Dinamik başlık algılandı: {video_title}")
        except:
            print("⚠️ Metadata okunamadı, varsayılan başlık kullanılıyor.")

    # 4. Video Dosyasını Kontrol Et
    video_path = "media/videos/final_output.mp4"
    if not os.path.exists(video_path):
        print("❌ HATA: Video dosyası bulunamadı!")
        return

    # 5. YouTube'a Yükleme Başlat
    request_body = {
        'snippet': {'title': video_title, 'description': video_description, 'tags': video_tags, 'categoryId': '27'},
        'status': {'privacyStatus': 'public', 'selfDeclaredMadeForKids': False}
    }

    try:
        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        response = youtube.videos().insert(part='snippet,status', body=request_body, media_body=media).execute()
        v_id = response.get('id')
        print(f"🎉 BAŞARI: Video yüklendi! ID: {v_id}")

        # 6. Kapak Fotoğrafını Ekle (s.png)
        if os.path.exists("s.png"):
            print("📸 Kapak ekleniyor...")
            time.sleep(20) # YouTube'un videoyu tanıması için bekleme
            youtube.thumbnails().set(videoId=v_id, media_body=MediaFileUpload("s.png")).execute()
            print("✅ Kapak başarıyla eklendi!")
    except Exception as e:
        print(f"⚠️ Yükleme hatası: {e}")

if __name__ == "__main__":
    upload_video()
