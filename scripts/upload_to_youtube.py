import os
import glob
import googleapiclient.discovery
import googleapiclient.http
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

# GitHub Secrets'tan alınacak çevresel değişkenler
CLIENT_ID = os.environ.get("YOUTUBE_CLIENT_ID")
CLIENT_SECRET = os.environ.get("YOUTUBE_CLIENT_SECRET")
REFRESH_TOKEN = os.environ.get("YOUTUBE_REFRESH_TOKEN")

def get_authenticated_service():
    """YouTube API servisini yetkilendirir ve başlatır."""
    if not all([CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN]):
        raise Exception("HATA: YouTube API anahtarları (Secrets) eksik!")

    creds = Credentials(
        None,
        refresh_token=REFRESH_TOKEN,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    )
    
    # Token süresi dolmuşsa yenile
    if not creds.valid:
        creds.refresh(Request())
        
    return googleapiclient.discovery.build("youtube", "v3", credentials=creds)

def upload_video():
    """Render edilen videoyu bulur ve YouTube'a yükler."""
    youtube = get_authenticated_service()
    
    # Render edilen videoyu bul (Manim varsayılan klasör yapısı)
    # media/videos/render_code/720p30/SceneName.mp4
    video_files = glob.glob("media/videos/**/*.mp4", recursive=True)
    
    if not video_files:
        print("Yüklenecek video dosyası bulunamadı!")
        return

    # En son oluşturulan videoyu seç
    video_path = video_files[0]
    print(f"Yükleme başlıyor: {video_path}")

    request_body = {
        "snippet": {
            "title": "Maarif Matematik - Yeni Ders (Otomatik)",
            "description": "İbrahim Soykan ile mantık odaklı matematik dersleri. Abone olmayı unutmayın!",
            "tags": ["matematik", "maarif", "eğitim", "lgs", "yks"],
            "categoryId": "27"  # Education kategorisi
        },
        "status": {
            "privacyStatus": "private",  # Kontrol etmen için başlangıçta gizli yükler
            "selfDeclaredMadeForKids": False
        }
    }

    # Video dosyasını yükleme hazırlığı
    media = googleapiclient.http.MediaFileUpload(
        video_path, 
        mimetype="video/mp4", 
        resumable=True
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Yükleme durumu: %{int(status.progress() * 100)}")

    print(f"BAŞARILI! Video yüklendi. Video ID: {response.get('id')}")

if __name__ == "__main__":
    try:
        upload_video()
    except Exception as e:
        print(f"HATA OLUŞTU: {e}")

