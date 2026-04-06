data = re.sub(r'\s+```$', '', data)
    return data.strip()

def upload_video():
    # 1. Video dosyasını bul
    video_files = glob.glob("media/videos/**/*.mp4", recursive=True)
    if not video_files:
        print("HATA: Yüklenecek video dosyası bulunamadı!")
        return
    
    video_path = video_files[0]
    print(f"Video bulundu: {video_path}")

    # 2. Ham verileri al ve temizle
    raw_token = os.environ.get('TOKEN_JSON')
    raw_client = os.environ.get('CLIENT_SECRETS_JSON')

    if not raw_token or not raw_client:
        print("HATA: GitHub Secrets (TOKEN_JSON veya CLIENT_SECRETS_JSON) boş!")
        return

    try:
        # JSON ayrıştırma
        token_str = clean_json_string(raw_token)
        client_str = clean_json_string(raw_client)
        
        creds_info = json.loads(token_str)
        client_info = json.loads(client_str)
        
        client_config = client_info.get('installed', client_info.get('web', {}))
        
        creds = Credentials(
            token=creds_info.get('token'),
            refresh_token=creds_info.get('refresh_token'),
            token_uri="[https://oauth2.googleapis.com/token](https://oauth2.googleapis.com/token)",
            client_id=client_config.get('client_id'),
            client_secret=client_config.get('client_secret'),
            scopes=['[https://www.googleapis.com/auth/youtube.upload](https://www.googleapis.com/auth/youtube.upload)']
        )
        
        youtube = build("youtube", "v3", credentials=creds)

        # Video başlığını dosya isminden al
        title = os.path.basename(video_path).replace('.mp4', '')

        request_body = {
            "snippet": {
                "title": f"Maarif Matematik - {title}",
                "description": "Maarif Modeli'ne uygun, mantık odaklı matematik dersi.",
                "categoryId": "27"
            },
            "status": {"privacyStatus": "unlisted"}
        }

        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        print("YouTube'a yükleme başlıyor...")
        response = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media
        ).execute()
        
        print(f"BAŞARILI! Video ID: {response.get('id')}")
        print(f"Video Linki: [https://youtu.be/](https://youtu.be/){response.get('id')}")
        
    except Exception as e:
        print(f"HATA OLUŞTU: {str(e)}")

if __name__ == "__main__":
    upload_video()
