import os
import glob
import json
import googleapiclient.discovery
import googleapiclient.http
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

# GitHub Secrets'tan gelen JSON metinlerini alıyoruz
CLIENT_SECRETS_STR = os.environ.get("CLIENT_SECRETS_JSON")
TOKEN_STR = os.environ.get("TOKEN_JSON")

def get_authenticated_service():
    """Mevcut JSON yapısından yetki bilgilerini ayıklar."""
    if not CLIENT_SECRETS_STR or not TOKEN_STR:
        raise Exception("HATA: CLIENT_SECRETS_JSON veya TOKEN_JSON GitHub Secrets'ta bulunamadı!")

    try:
        # JSON metinlerini Python sözlüğüne çeviriyoruz
        client_data = json.loads(CLIENT_SECRETS_STR)
        token_data = json.loads(TOKEN_STR)
        
        # Standart Google JSON yapısından gerekli alanları çekiyoruz
        # Not: JSON yapınız farklıysa buradan ayar yapılabilir
        client_id = client_data.get("installed", {}).get("client_id") or client_data.get("web", {}).get("client_id")
        client_secret = client_data.get("installed", {}).get("client_secret") or client_data.get("web", {}).get("client_secret")
        refresh_token = token_data.get("refresh_token")

        if not all([client_id, client_secret, refresh_token]):
            raise Exception("JSON dosyalarının içinde gerekli alanlar (client_id, secret, refresh_token) eksik!")

        creds = Credentials(
            None,
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=client_id,
            client_secret=client_secret,
            scopes=["https://www.googleapis.com/auth/youtube.upload"]
        )
        
        if not creds.valid:
            creds.refresh(Request())
            
        return googleapiclient.discovery.build("youtube", "v3", credentials=creds)
        
    except json.JSONDecodeError:
        raise Exception("GitHub Secrets'a yapıştırılan metin geçerli bir JSON değil!")

def upload_video():
    """Render edilen videoyu bulur ve YouTube'a yükler."""
    youtube = get_authenticated_service()
    
    # En güncel videoyu bul
    video_files = glob.glob("media/videos/**/*.mp4", recursive=True)
    
    if not video_files:
        print("Yüklenecek video dosyası bulunamadı!")
        return

    video_path = video_files[0]
    print(f"Yükleme başlıyor: {video_path}")

    request_body = {
        "snippet": {
            "title": "Maarif Matematik - Otomatik Ders",
            "description": "Maarif Modeli'ne uygun ders içeriği. Abone olmayı unutmayın!",
            "categoryId": "27" 
        },
        "status": {
            "privacyStatus": "private" 
        }
    }

    media = googleapiclient.http.MediaFileUpload(video_path, mimetype="video/mp4", resumable=True)
    request = youtube.videos().insert(part="snippet,status", body=request_body, media_body=media)

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Yükleme: %{int(status.progress() * 100)}")

    print(f"BAŞARILI! Video ID: {response.get('id')}")

if __name__ == "__main__":
    try:
        upload_video()
    except Exception as e:
        print(f"KRİTİK HATA: {e}")

