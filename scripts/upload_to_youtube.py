import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# ⚠️ YETKİ KAPSAMI: YouTube videolarını yönetmek için tam yetki
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def upload_video():
    try:
        # 1. GitHub Secrets üzerinden Token verisini çek
        t_json = os.environ.get('TOKEN_JSON')
        if not t_json:
            print("❌ HATA: TOKEN_JSON bulunamadı! GitHub Secrets ayarlarınızı kontrol edin.")
            return

        token_data = json.loads(t_json)
        # Token içindeki yetki kapsamını (scope) zorunlu olarak güncelliyoruz
        token_data['scopes'] = SCOPES 
        creds = Credentials.from_authorized_user_info(token_data, SCOPES)
        
        # Eğer erişim anahtarının süresi dolmuşsa otomatik yenile
        if creds and creds.expired and creds.refresh_token:
            print("🔄 Erişim anahtarı yenileniyor...")
            creds.refresh(Request())
            
        youtube = build('youtube', 'v3', credentials=creds)
        print("✅ YouTube API bağlantısı başarıyla kuruldu.")
        
        # 2. Standart Bilgiler (metadata.json yoksa yedek olarak kullanılır)
        video_path = "media/videos/final_output.mp4"
        title = "İbrahim Soykan | Maarif Matematik - Yeni Ders"
        description = "Mantık odaklı, ezbersiz matematik anlatımı."
        tags = ["matematik", "maarif matematik", "eğitim"]
        
        # 3. Dinamik Metadata Okuma
        # Make.com'un gönderdiği metadata.json dosyasını açıyoruz
        if os.path.exists('metadata.json'):
            try:
                with open('metadata.json', 'r', encoding='utf-8') as f:
                    m = json.load(f)
                    title = m.get('title', title)
                    description = m.get('description', description)
                    # Tags listeyse birleştir, değilse olduğu gibi al
                    raw_tags = m.get('tags', tags)
                    tags = raw_tags if isinstance(raw_tags, list) else tags
                    print(f"📄 Dinamik Veri Alındı: {title}")
            except Exception as e:
                print(f"⚠️ metadata.json okunamadı, standart başlık kullanılıyor: {e}")

        # 4. YouTube Yükleme Ayarları
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags,
                'categoryId': '27' # Eğitim Kategorisi
            },
            'status': {
                'privacyStatus': 'unlisted', # ✅ HER ZAMAN LİSTE DIŞI (Siz kontrol ettikten sonra yayına alırsınız)
                'selfDeclaredMadeForKids': False
            }
        }

        # 5. Video Dosyası Kontrolü ve Yükleme
        if not os.path.exists(video_path):
            print(f"❌ HATA: Video dosyası bulunamadı: {video_path}")
            return

        print(f"🚀 Video yükleniyor: {title}...")
        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        request = youtube.videos().insert(part='snippet,status', body=body, media_body=media)
        
        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"⌛ Yükleme Durumu: %{int(status.progress() * 100)}")

        video_id = response.get('id')
        print(f"🎉 BAŞARI! Video yüklendi. Video ID: {video_id}")

        # 6. Kapak Fotoğrafı (s.png) Ekleme
        # YouTube'un videoyu işlemesi için kısa bir süre bekliyoruz
        if os.path.exists("s.png"):
            print("🖼️ Kapak fotoğrafı yükleniyor...")
            time.sleep(10) # İşlem süresi tanımak için 10 saniye bekleme
            try:
                youtube.thumbnails().set(
                    videoId=video_id,
                    media_body=MediaFileUpload("s.png")
                ).execute()
                print("✅ Kapak fotoğrafı (s.png) başarıyla eklendi.")
            except Exception as thumb_err:
                print(f"⚠️ Kapak fotoğrafı yüklenemedi: {thumb_err}")

    except Exception as e:
        print(f"❌ KRİTİK SİSTEM HATASI: {e}")

if __name__ == "__main__":
    upload_video()
