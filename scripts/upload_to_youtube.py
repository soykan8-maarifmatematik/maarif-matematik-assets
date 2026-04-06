import os
import json
import glob
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload

def upload_video():
    # 1. Video dosyasını bul (Manim çıktısı)
    video_files = glob.glob("media/videos/**/*.mp4", recursive=True)
    if not video_files:
        print("HATA: Yüklenecek video dosyası bulunamadı!")
        return
    
    video_path = video_files[0]
    print(f"Video bulundu: {video_path}")

    # 2. Kimlik Bilgilerini GitHub Secrets'tan Al
    token_data = os.environ.get('TOKEN_JSON')
    client_data = os.environ.get('CLIENT_SECRETS_JSON')

    if not token_data or not client_data:
        print("HATA: GitHub Secrets (TOKEN_JSON veya CLIENT_SECRETS_JSON) eksik!")
        return

    # JSON verilerini yükle
    try:
        creds_info = json.loads(token_data)
        client_info = json.loads(client_data)
        
        # Desktop app yapısında client_id ve secret 'installed' altındadır
        client_config = client_info.get('installed', client_info.get('web', {}))
        
        creds = Credentials(
            token=creds_info.get('token'),
            refresh_token=creds_info.get('refresh_token'),
            token_uri="https://oauth2.googleapis.com/token",
            client_id=client_config.get('client_id'),
            client_secret=client_config.get('client_secret'),
            scopes=['https://www.googleapis.com/auth/youtube.upload']
        )
    except Exception as e:
        print(f"JSON Ayrıştırma Hatası: {e}")
        return

    # 3. YouTube API Bağlantısı
    youtube = build("youtube", "v3", credentials=creds)

    request_body = {
        "snippet": {
            "title": "Maarif Matematik - Yeni Ders (Otomatik)",
            "description": "Bu video Maarif Matematik otomasyonu tarafından üretilmiştir.",
            "categoryId": "27", # Education
            "tags": ["matematik", "maarif", "lgs", "yks"]
        },
        "status": {
            "privacyStatus": "unlisted",
            "selfDeclaredMadeForKids": False
        }
    }

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
    
    print("YouTube'a yükleme başlıyor...")
    try:
        response = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media
        ).execute()
        print(f"BAŞARILI! Video ID: {response.get('id')}")
        print(f"Video Linki: https://youtu.be/{response.get('id')}")
    except Exception as e:
        print(f"Yükleme sırasında hata oluştu: {e}")

if __name__ == "__main__":
    upload_video()
