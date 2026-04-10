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

    # Metadata.json Dosyasını Oku (Hata Payını Sıfırlayan Okuma)
    video_title = "Maarif Matematik - Yeni Ders"
    video_description = "Maarif Modeli'ne uygun, mantık odaklı matematik içeriği."
    video_tags = ["matematik", "maarif"]

    try:
        with open('metadata.json', 'r', encoding='utf-8') as f:
            metadata = json.load(f)
            # Eğer JSON yapısı nested (iç içe) ise veya düz ise her iki durumu da kontrol et
            video_title = metadata.get('title', metadata.get('metadata', {}).get('title', video_title))
            video_description = metadata.get('description', metadata.get('metadata', {}).get('description', video_description))
            video_tags = metadata.get('tags', metadata.get('metadata', {}).get('tags', video_tags))
    except Exception as e:
        print(f"Metadata okuma hatası: {e}. Varsayılan başlık kullanılıyor.")

    # Video Dosyasını Bul
    video_file = "media/videos/final_output.mp4"
    if not os.path.exists(video_file):
        print("HATA: Video dosyası bulunamadı!")
        return

    print(f"YouTube'a yükleniyor: {video_title}")

    # Video Yükleme İsteği
    request_body = {
        'snippet': {
            'title': video_title,
            'description': video_description,
            'tags': video_tags,
            'categoryId': '27' # Eğitim kategorisi
        },
        'status': {
            'privacyStatus': 'public', # 'private' veya 'unlisted' yapabilirsin test için
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
    print(f"Video başarıyla yüklendi! ID: {video_id}")

    # --- KAPAK FOTOĞRAFI (Thumbnail) YÜKLEME ---
    thumbnail_file = "s.png"
    if os.path.exists(thumbnail_file):
        print(f"Kapak fotoğrafı yükleniyor: {thumbnail_file}")
        try:
            # YouTube bazen video işlenmeden kapağı kabul etmez, kısa bir bekleme
            time.sleep(5)
            youtube.thumbnails().set(
                videoId=video_id,
                media_body=MediaFileUpload(thumbnail_file)
            ).execute()
            print("Kapak fotoğrafı başarıyla güncellendi!")
        except Exception as e:
            print(f"Kapak fotoğrafı yüklenirken hata oluştu: {e}")
    else:
        print("Uyarı: s.png bulunamadı, özel kapak yüklenemedi.")

if __name__ == "__main__":
    upload_video()
