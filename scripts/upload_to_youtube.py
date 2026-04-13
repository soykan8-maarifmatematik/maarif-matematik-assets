import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# ⚠️ YETKİ ADRESİ (Scope) - Bu adres anahtar.py ile milimetrik aynı olmalı
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def upload_video():
    try:
        # 1. GitHub Secrets verilerini çek
        t_json = os.environ.get('TOKEN_JSON')
        cs_json = os.environ.get('CLIENT_SECRETS_JSON')
        
        if not t_json:
            print("❌ HATA: TOKEN_JSON GitHub Secret bulunamadı!")
            return

        # JSON verisini yükle
        token_data = json.loads(t_json)
        
        # 🛡️ YETKİ TAMİRİ: Token içindeki yetkiyi kodla aynı yapmaya zorluyoruz
        # Bu satır, "invalid_scope" hatasını aşmamızı sağlayan en kritik parçadır.
        token_data['scopes'] = SCOPES 
        
        creds = Credentials.from_authorized_user_info(token_data, SCOPES)
        
        # Eğer anahtarın süresi dolmuşsa yenile
        if creds and creds.expired and creds.refresh_token:
            print("🔄 Anahtar süresi dolmuş, YouTube'dan taze onay alınıyor...")
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"❌ YENİLEME HATASI: {e}")
                return
            
        youtube = build('youtube', 'v3', credentials=creds)
        print("✅ YouTube bağlantısı başarıyla kuruldu.")
        
        # 2. Dosya ve Metadata Ayarları
        video_path = "media/videos/final_output.mp4"
        title = "Birim Kesirler Mantığı | Maarif Matematik"
        description = "Maarif Modeli'ne uygun, mantık odaklı anlatım."
        
        # Eğer metadata.json varsa bilgileri oradan çek
        if os.path.exists('metadata.json'):
            try:
                with open('metadata.json', 'r', encoding='utf-8') as f:
                    m = json.load(f)
                    title = m.get('title', title)
                    description = m.get('description', description)
                    print(f"📄 Metadata okundu: {title}")
            except:
                print("⚠️ metadata.json okunamadı, varsayılanlar kullanılıyor.")

        if not os.path.exists(video_path):
            print(f"❌ HATA: Video dosyası bulunamadı: {video_path}")
            return

        # 3. Yükleme Paketi Hazırlığı
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'categoryId': '27' # Eğitim kategorisi
            },
            'status': {
                'privacyStatus': 'public',
                'selfDeclaredMadeForKids': False
            }
        }

        print(f"🚀 Video yükleniyor: {title}")
        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        request = youtube.videos().insert(part='snippet,status', body=body, media_body=media)
        
        response = request.execute()
        video_id = response.get('id')
        print(f"🎉 BAŞARI! Video YouTube'da yayında. ID: {video_id}")

        # 4. Kapak Fotoğrafı (Eğer s.png varsa)
        if os.path.exists("s.png"):
            print("📸 Kapak fotoğrafı yükleniyor...")
            time.sleep(10) # YouTube'un videoyu tanıması için kısa bir bekleme
            youtube.thumbnails().set(
                videoId=video_id,
                media_body=MediaFileUpload("s.png")
            ).execute()
            print("✅ Kapak fotoğrafı başarıyla eklendi!")

    except Exception as e:
        print(f"❌ KRİTİK HATA: {e}")

if __name__ == "__main__":
    upload_video()
