import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video():
    # 1. Kimlik Bilgileri
    try:
        client_secrets = json.loads(os.environ.get('CLIENT_SECRETS_JSON'))
        token_data = json.loads(os.environ.get('TOKEN_JSON'))
        creds = Credentials.from_authorized_user_info(token_data)
        youtube = build('youtube', 'v3', credentials=creds)
    except Exception as e:
        print(f"HATA: Yetki alınamadı: {e}")
        return

    # 2. Varsayılanlar
    video_title = "Birim Kesirler Mantığı | Maarif Matematik"
    video_description = "Maarif Modeli'ne uygun matematik dersi."
    video_tags = ["matematik", "ders"]

    # 3. METADATA BULUCU (GELİŞMİŞ)
    # GitHub Actions ana dizinde çalıştığı için direkt kök dizine bakıyoruz
    current_dir = os.getcwd()
    metadata_path = os.path.join(current_dir, 'metadata.json')
    
    print(f"BİLGİ: Dosya şu adreste aranıyor: {metadata_path}")

    if os.path.exists(metadata_path):
        try:
            with open(metadata_path, 'r', encoding='utf-8') as f:
                raw_data = f.read().strip()
                print(f"BİLGİ: Dosya bulundu. Ham İçerik: {raw_data[:50]}...")
                
                # Eğer dosya sadece "{object}" veya boşsa hata verir
                metadata = json.loads(raw_data)
                
                # Make.com'dan gelen yapıyı kontrol et
                m = metadata.get('metadata', metadata)
                
                t = m.get('title')
                d = m.get('description')
                tg = m.get('tags')

                if t: video_title = t
                if d: video_description = d
                if tg: video_tags = tg
                print(f"✅ BAŞARILI: Dinamik başlık okundu: {video_title}")
        except Exception as e:
            print(f"⚠️ Dosya bulundu ama JSON hatası var: {e}")
    else:
        print(f"❌ HATA: metadata.json dosyası fiziki olarak yok! Mevcut dosyalar: {os.listdir(current_dir)}")

    # 4. VİDEO YÜKLEME
    video_file = "media/videos/final_output.mp4"
    if not os.path.exists(video_file):
        print("HATA: Video dosyası render edilememiş!")
        return

    request_body = {
        'snippet': {'title': video_title, 'description': video_description, 'tags': video_tags, 'categoryId': '27'},
        'status': {'privacyStatus': 'public', 'selfDeclaredMadeForKids': False}
    }

    try:
        media = MediaFileUpload(video_file, chunksize=-1, resumable=True)
        response = youtube.videos().insert(part='snippet,status', body=request_body, media_body=media).execute()
        video_id = response.get('id')
        print(f"🎉 VİDEO YÜKLENDİ! Video ID: {video_id}")

        # 5. KAPAK FOTOĞRAFI (s.png)
        # s.png ana dizinde olduğu için direkt kontrol ediyoruz
        if os.path.exists("s.png"):
            print("📸 Kapak ekleniyor (s.png)...")
            time.sleep(25) # YouTube'un videoyu tanıması için bekleme süresi arttırıldı
            youtube.thumbnails().set(videoId=video_id, media_body=MediaFileUpload("s.png")).execute()
            print("✅ Kapak başarıyla güncellendi!")
        else:
            print(f"❌ UYARI: s.png bulunamadı! Mevcut dosyalar: {os.listdir(current_dir)}")

    except Exception as e:
        print(f"⚠️ YouTube işlemi sırasında hata: {e}")

if __name__ == "__main__":
    upload_video()
