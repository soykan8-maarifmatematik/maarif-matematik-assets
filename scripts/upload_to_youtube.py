import os
import glob
import json
import googleapiclient.discovery
import googleapiclient.http
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

CLIENT_SECRETS_STR = os.environ.get("CLIENT_SECRETS_JSON", "").strip()
TOKEN_STR = os.environ.get("TOKEN_JSON", "").strip()

def get_authenticated_service():
    if not CLIENT_SECRETS_STR or not TOKEN_STR:
        raise Exception("HATA: Secrets eksik!")
    
    client_data = json.loads(CLIENT_SECRETS_STR)
    inner = client_data.get("installed") or client_data.get("web") or client_data
    
    if TOKEN_STR.startswith('{'):
        refresh_token = json.loads(TOKEN_STR).get("refresh_token")
    else:
        refresh_token = TOKEN_STR

    creds = Credentials(
        None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=inner.get("client_id"),
        client_secret=inner.get("client_secret"),
        scopes=["https://www.googleapis.com/auth/youtube.upload"]
    )
    if not creds.valid: creds.refresh(Request())
    return googleapiclient.discovery.build("youtube", "v3", credentials=creds)

def upload_video():
    youtube = get_authenticated_service()
    
    # 1. Zengin Metadata Bilgilerini Oku
    # Make.com bu dosyayı oluşturup göndermeli
    try:
        with open("metadata.json", "r", encoding="utf-8") as f:
            meta = json.load(f)
            title = meta.get("title", "Maarif Matematik - Yeni Ders")
            description = meta.get("description", "Maarif Modeli matematik anlatımı.")
            tags = meta.get("tags", ["matematik", "maarif"])
    except:
        print("BİLGİ: metadata.json bulunamadı, varsayılanlar kullanılıyor.")
        title = "Maarif Matematik - İbrahim Soykan Yeni Ders"
        description = "Maarif Modeli'ne uygun matematik içeriği."
        tags = ["matematik"]

    # 2. Videoyu Bul
    video_files = glob.glob("media/videos/**/*.mp4", recursive=True)
    if not video_files: return print("Video yok!")
    video_path = video_files[0]

    print(f"Yükleniyor: {title}")

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "27"
        },
        "status": {"privacyStatus": "private"}
    }

    media = googleapiclient.http.MediaFileUpload(video_path, mimetype="video/mp4", resumable=True)
    request = youtube.videos().insert(part="snippet,status", body=request_body, media_body=media)

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status: print(f"İlerleme: %{int(status.progress() * 100)}")

    print(f"BAŞARILI! Video ID: {response.get('id')}")

if __name__ == "__main__":
    upload_video()
