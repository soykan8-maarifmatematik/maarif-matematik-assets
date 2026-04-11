import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video():
    # 1. Kimlik Bilgilerini Yükle
    try:
        client_secrets_raw = os.environ.get('CLIENT_SECRETS_JSON')
        token_data_raw = os.environ.get('TOKEN_JSON')
        
        if not client_secrets_raw or not token_data_raw:
            print("HATA: YouTube API anahtarları GitHub Secrets içinde bulunamadı!")
            return

        client_secrets = json.loads(client_secrets_raw)
        token_data = json.loads(token_data_raw)
        
        creds = Credentials.from_authorized_user_info(token_data)
        youtube = build('youtube', 'v3', credentials=creds)
    except Exception as e:
        print(f"HATA: Yetkilendirme veya JSON yükleme hatası: {e}")
        return

    # 2. Varsayılan (Yedek) Değerler - İsimsiz
    video_title = "Birim Kesirler Mantığı | Maarif Matematik"
    video_description = "Maarif Modeli'ne uygun, mantık odaklı matematik dersleri. Ezberden uzak, keşfederek öğrenme."
    video_tags = ["matematik", "ders", "maarif"]

    # 3. metadata.json Dosyasını Bul ve Oku
    # GitHub Actions ortamında dosya nerede olursa olsun bulmaya çalışır.
    possible_paths = [
        'metadata.json', 
        './metadata.json', 
        'scripts/metadata.json',
        os.path.join(os.getcwd(), 'metadata.json')
    ]
    
    metadata_found = False
    for path in possible_paths:
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content:
                        metadata = json.loads(content)
                        # Make.com'dan gelen 'metadata' objesini veya doğrudan anahtarları kontrol et
                        m = metadata.get('metadata', metadata)
                        
                        t = m.get('title')
                        d = m.get('description')
                        tg = m.get('tags')

                        if t: video_title = t
                        if d: video_description = d
                        if tg: video_tags = tg
                        metadata_found = True
                        print(f"✅ BAŞARILI: Metadata şu yoldan okundu: {path}")
                        break
            except Exception as e:
                print(f"⚠️ Dosya bulundu ama okunamadı ({path}): {e}")
                continue

    if not metadata_found:
        print("❌ UYARI: metadata.json dosyası bulunamadı! İsimsiz yedek başlık kullanılıyor.")

    # 4. Video Dosyasını Kontrol Et
    video_file = "media/videos/final_output.mp4"
    if not os.path.exists(video_file):
        print(f"HATA: Video dosyası bulunamadı! Yol: {video_file}")
        return

    # 5. YouTube Yükleme İşlemi
    print(f"🚀 YouTube'a Yükleme Başlıyor: {video_title}")
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

    try:
        media = MediaFileUpload(video_file, chunksize=-1, resumable=True)
        response_upload = youtube.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=media
        ).execute()

        video_id = response_upload.get('id')
        print(f"🎉 VİDEO BAŞARIYLA YÜKLENDİ! Video ID: {video_id}")

        # 6. Özel Kapak (s.png) Yükleme
        thumbnail_file = "s.png"
        if os.path.exists(thumbnail_file):
            print(f"📸 Kapak fotoğrafı yükleniyor: {thumbnail_file}")
            # YouTube API senkronizasyonu için bekleme (Önemli!)
            time.sleep(15) 
            try:
                youtube.thumbnails().set(
                    videoId=video_id,
                    media_body=MediaFileUpload(thumbnail_file)
                ).execute()
                print("✅ Kapak fotoğrafı başarıyla güncellendi!")
            except Exception as e:
                print(f"⚠️ Kapak fotoğrafı yüklenirken hata oluştu: {e}")
        else:
            print("ℹ️ BİLGİ: s.png (kapak) bulunamadı.")

    except Exception as e:
        print(f"HATA: YouTube yükleme sırasında bir sorun oluştu: {e}")

if __name__ == "__main__":
    upload_video()
