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

    # --- VARSAYILAN YEDEK DEĞERLER (FALLBACK) ---
    video_title = "Maarif Matematik - Yeni Ders"
    video_description = "Maarif Modeli'ne uygun, mantık odaklı matematik içeriği."
    video_tags = ["matematik", "maarif"]

    # metadata.json Dosyasını Dinamik Olarak Oku
    try:
        if os.path.exists('metadata.json'):
            with open('metadata.json', 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"DEBUG: Okunan ham metadata: {content[:100]}...") # Loglarda kontrol için
                metadata = json.loads(content)
                
                # Hem düz hem de iç içe (nested) JSON yapılarını kontrol et
                new_title = metadata.get('title', metadata.get('metadata', {}).get('title'))
                new_desc = metadata.get('description', metadata.get('metadata', {}).get('description'))
                new_tags = metadata.get('tags', metadata.get('metadata', {}).get('tags'))

                if new_title: video_title = new_title
                if new_desc: video_description = new_desc
                if new_tags: video_tags = new_tags
                
                print(f"BAŞARILI: Dinamik başlık alındı -> {video_title}")
        else:
            print("UYARI: metadata.json bulunamadı, varsayılan başlık kullanılıyor.")
    except Exception as e:
        print(f"HATA: Metadata işlenirken sorun oluştu: {e}")

    # Video Dosyasını Bul
    video_file = "media/videos/final_output.mp4"
    if not os.path.exists(video_file):
        print("HATA: Video dosyası bulunamadı!")
        return

    print(f"YouTube'a yükleme işlemi başlıyor: {video_title}")

    # Video Yükleme İsteği
    request_body = {
        'snippet': {
            'title': video_title,
            'description': video_description,
            'tags': video_tags,
            'categoryId': '27' # Eğitim
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
    print(f"Video başarıyla yüklendi! ID: {video_id}")

    # --- KAPAK FOTOĞRAFI (Thumbnail) YÜKLEME ---
    thumbnail_file = "s.png"
    if os.path.exists(thumbnail_file):
        print(f"Kapak fotoğrafı yükleniyor: {thumbnail_file}")
        try:
            # YouTube API senkronizasyonu için kısa bekleme
            time.sleep(7)
            youtube.thumbnails().set(
                videoId=video_id,
                media_body=MediaFileUpload(thumbnail_file)
            ).execute()
            print("Kapak fotoğrafı başarıyla güncellendi!")
        except Exception as e:
            print(f"Kapak fotoğrafı yüklenirken hata oluştu: {e}")
    else:
        print("BİLGİ: s.png bulunamadı, özel kapak yüklenemedi.")

if __name__ == "__main__":
    upload_video()
