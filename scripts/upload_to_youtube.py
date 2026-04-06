import os
import glob
import json
import googleapiclient.discovery
import googleapiclient.http
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

# GitHub Secrets'tan gelen veriler
CLIENT_SECRETS_STR = os.environ.get("CLIENT_SECRETS_JSON", "").strip()
TOKEN_STR = os.environ.get("TOKEN_JSON", "").strip()

def parse_json_safely(data_str, name):
    """Metni JSON olarak okumaya çalışır, olmazsa hata detayını verir."""
    if not data_str:
        raise Exception(f"HATA: {name} boş! GitHub Secrets'ı kontrol edin.")
    
    try:
        # Eğer veri zaten { ile başlıyorsa JSON'dır
        if data_str.startswith('{'):
            return json.loads(data_str)
        else:
            # Eğer { ile başlamıyorsa, kullanıcı sadece ham tokenı yapıştırmış olabilir
            if name == "TOKEN_JSON":
                print(f"BİLGİ: {name} bir JSON objesi değil, ham metin olarak değerlendiriliyor.")
                return {"refresh_token": data_str}
            else:
                raise Exception(f"{name} bir JSON formatında ({{...}}) olmalı!")
    except json.JSONDecodeError as e:
        # Hata anında metnin başını göstererek kullanıcıya ipucu verelim
        snippet = data_str[:15] + "..."
        raise Exception(f"HATA: {name} geçersiz JSON formatı! Başlangıcı: '{snippet}'. Hata: {e}")

def get_authenticated_service():
    client_data = parse_json_safely(CLIENT_SECRETS_STR, "CLIENT_SECRETS_JSON")
    token_data = parse_json_safely(TOKEN_STR, "TOKEN_JSON")
    
    # Client ID ve Secret ayıklama (web veya installed formatı için)
    inner_data = client_data.get("installed") or client_data.get("web") or client_data
    client_id = inner_data.get("client_id")
    client_secret = inner_data.get("client_secret")
    refresh_token = token_data.get("refresh_token")

    if not all([client_id, client_secret, refresh_token]):
        raise Exception("HATA: JSON içeriğinde client_id, client_secret veya refresh_token eksik!")

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

def upload_video():
    try:
        youtube = get_authenticated_service()
        video_files = glob.glob("media/videos/**/*.mp4", recursive=True)
        
        if not video_files:
            print("Yüklenecek video bulunamadı!")
            return

        video_path = video_files[0]
        print(f"Yükleme başlıyor: {video_path}")

        request_body = {
            "snippet": {
                "title": "Maarif Matematik - İbrahim Soykan Yeni Ders",
                "description": "Maarif Modeli'ne uygun matematik içeriği.",
                "categoryId": "27" 
            },
            "status": {"privacyStatus": "private"}
        }

        media = googleapiclient.http.MediaFileUpload(video_path, mimetype="video/mp4", resumable=True)
        request = youtube.videos().insert(part="snippet,status", body=request_body, media_body=media)

        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"Yükleme durumu: %{int(status.progress() * 100)}")

        print(f"BAŞARILI! Video YouTube'a yüklendi. ID: {response.get('id')}")
    except Exception as e:
        print(f"KRİTİK HATA: {e}")

if __name__ == "__main__":
    upload_video()
