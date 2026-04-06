import os
import glob
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

# GitHub Secrets'tan gelecek bilgiler
CLIENT_ID = os.environ.get("YOUTUBE_CLIENT_ID")
CLIENT_SECRET = os.environ.get("YOUTUBE_CLIENT_SECRET")
REFRESH_TOKEN = os.environ.get("YOUTUBE_REFRESH_TOKEN")

def get_authenticated_service():
    creds = Credentials(
        None,
        refresh_token=REFRESH_TOKEN,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    )
    
    if not creds.valid:
        creds.refresh(Request())
        
    return googleapiclient.discovery.build("youtube", "v3", credentials=creds)

def upload_video():
    youtube = get_authenticated_service()
    
    # Render edilen videoyu bul
    video_files = glob.glob("media/videos/**/*.mp4", recursive=True)
    if not video_files:
        print("HATA: Yüklenecek video dosyası bulunamadı!")
        return

    video_path = video_files[0]
    print(f"Video yükleniyor: {video_path}")

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "categoryId": "27", # Eğitim kategorisi
                "description": "Maarif Matematik - İbrahim Soykan ile mantık odaklı matematik dersleri.",
                "title": "Maarif Matematik Yeni Ders (Otomatik Yükleme)",
                "tags": ["matematik", "maarif", "eğitim", "lgs", "yks"]
            },
            "status": {
                "privacyStatus": "private" # İlk yüklemede 'gizli' yapalım, kontrol edip açarsınız.
            }
        },
        media_body=googleapiclient.http.MediaFileUpload(video_path, chunksize=-1, resumable=True)
    )
    
    response = request.execute()
    print(f"BAŞARILI! Video ID: {response['id']}")

if __name__ == "__main__":
    try:
        upload_video()
    except Exception as e:
        print(f"YouTube Yükleme Hatası: {e}")

