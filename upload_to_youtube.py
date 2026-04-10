import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video():
    # Kimlik Bilgilerini Yükle
    client_secrets = json.loads(os.environ.get('CLIENT_SECRETS_JSON'))
    token_data = json.loads(os.environ.get('TOKEN_JSON'))
    
    creds = Credentials.from_authorized_user_info(token_data)
    youtube = build('youtube', 'v3', credentials=creds)

    # --- YENİ YEDEK DEĞERLER (İSİMSİZ) ---
    video_title = "Maarif Matematik - Güncel Ders"
    video_description = "Maarif Modeli'ne uygun, mantık odaklı matematik dersleri."
    video_tags = ["matematik", "ders", "maarif"]

    # metadata.json Dosyasını Akıllıca Oku
    if os.path.exists('metadata.json'):
        try:
            with open('metadata.json', 'r', encoding='utf-8') as f:
                content = f.read().strip()
                # Eğer dosya boş değilse parse et
                if content:
                    metadata = json.loads(content)
                    
                    # Veriyi çek (Hangi formatta olursa olsun)
                    t = metadata.get('title') or metadata.get('metadata', {}).get('title')
                    d = metadata.get('description') or metadata.get('metadata', {}).get('description')
                    tg = metadata.get('tags') or metadata.get('metadata', {}).get('tags')

                    if t: video_title = t
                    if d: video_description = d
                    if tg: video_tags = tg
                    print(f"BAŞARILI: Dinamik başlık okundu: {video_title}")
        except Exception as e:
            print(f"UYARI: Metadata parse edilemedi (JSON hatası olabilir): {e}")
    else:
        print("BİLGİ: metadata.json bulunamadı.")

    # Video Dosyasını Kontrol Et
    video_file = "media/videos/final_output.mp4"
    if not os.path.exists(video_file):
        print("HATA: Video dosyası (final_output.mp4) bulunamadı!")
        return

    # Video Yükleme
    print(f"Yükleme Başlıyor: {video_title}")
    request_body = {
        'snippet': {
            'title': video_title,
            'description': video_description,
            'tags': video_tags,
            'categoryId': '27'
        },
        'status': {
            'privacyStatus': 'public',
            'selfDeclaredMadeForKids': False
        }
    }

    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)
    response_upload = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media
    ).execute()

    video_id = response_upload.get('id')
    print(f"Video yüklendi! ID: {video_id}")

    # --- KAPAK FOTOĞRAFI (s.png) ---
    thumbnail_file = "s.png"
    if os.path.exists(thumbnail_file):
        print(f"Kapak yükleniyor: {thumbnail_file}")
        # YouTube'un videoyu işlemesi için 10 saniye bekle
        time.sleep(10)
        try:
            youtube.thumbnails().set(
                videoId=video_id,
                media_body=MediaFileUpload(thumbnail_file)
            ).execute()
            print("Kapak başarıyla eklendi!")
        except Exception as e:
            print(f"Kapak yükleme hatası: {e}")

if __name__ == "__main__":
    upload_video()
