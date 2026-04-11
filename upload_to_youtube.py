import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video():
    # 1. Yetki Kontrolü
    try:
        client_secrets = json.loads(os.environ.get('CLIENT_SECRETS_JSON'))
        token_data = json.loads(os.environ.get('TOKEN_JSON'))
        creds = Credentials.from_authorized_user_info(token_data)
        youtube = build('youtube', 'v3', credentials=creds)
    except Exception as e:
        print(f"HATA: Yetki alınamadı: {e}")
        return

    # 2. YEDEK DEĞERLER (İsimsiz ve Daha Profesyonel)
    video_title = "Birim Kesirler Mantığı | Maarif Matematik"
    video_description = "Maarif Modeli'ne uygun, mantık odaklı matematik dersleri."
    video_tags = ["matematik", "ders", "maarif"]

    # 3. METADATA ARAMA (Dinamik Başlık İçin)
    # GitHub'da dosya listenin en üstünde duran metadata.json'ı bulmaya çalışır
    m_path = 'metadata.json'
    if os.path.exists(m_path):
        try:
            with open(m_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                m = data.get('metadata', data)
                video_title = m.get('title', video_title)
                video_description = m.get('description', video_description)
                video_tags = m.get('tags', video_tags)
                print(f"✅ BAŞARILI: Dinamik başlık okundu: {video_title}")
        except:
            print("⚠️ Metadata dosyası bozuk veya okunamadı.")
    else:
        print("❌ HATA: metadata.json bulunamadı, yedek başlık kullanılıyor.")

    # 4. VİDEO YÜKLEME
    v_file = "media/videos/final_output.mp4"
    if not os.path.exists(v_file):
        print("HATA: Video dosyası yok!")
        return

    print(f"🚀 Yükleme Başlıyor: {video_title}")
    request_body = {
        'snippet': {'title': video_title, 'description': video_description, 'tags': video_tags, 'categoryId': '27'},
        'status': {'privacyStatus': 'public', 'selfDeclaredMadeForKids': False}
    }

    try:
        media = MediaFileUpload(v_file, chunksize=-1, resumable=True)
        response = youtube.videos().insert(part='snippet,status', body=request_body, media_body=media).execute()
        video_id = response.get('id')
        print(f"🎉 VİDEO YÜKLENDİ! ID: {video_id}")

        # 5. KAPAK FOTOĞRAFI (s.png)
        if os.path.exists("s.png"):
            print("📸 Kapak ekleniyor...")
            time.sleep(20) # YouTube'un videoyu tanıması için süre arttırıldı
            youtube.thumbnails().set(videoId=video_id, media_body=MediaFileUpload("s.png")).execute()
            print("✅ Kapak başarıyla eklendi!")
    except Exception as e:
        print(f"⚠️ Hata oluştu: {e}")

if __name__ == "__main__":
    upload_video()
