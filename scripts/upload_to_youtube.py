import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# ⚠️ YETKİ KAPSAMI
SCOPES = ['[https://www.googleapis.com/auth/youtube.force-ssl](https://www.googleapis.com/auth/youtube.force-ssl)']

def upload_video():
    try:
        t_json = os.environ.get('TOKEN_JSON')
        if not t_json:
            print("❌ HATA: TOKEN_JSON bulunamadı!")
            return

        token_data = json.loads(t_json)
        token_data['scopes'] = SCOPES 
        creds = Credentials.from_authorized_user_info(token_data, SCOPES)
        
        if creds and creds.expired and creds.refresh_token:
            print("🔄 Erişim anahtarı yenileniyor...")
            creds.refresh(Request())
            
        youtube = build('youtube', 'v3', credentials=creds)
        print("✅ YouTube API bağlantısı başarıyla kuruldu.")
        
        video_path = "media/videos/final_output.mp4"
        title = "İbrahim Soykan | Maarif Matematik - Yeni Ders"
        description = "Mantık odaklı, ezbersiz matematik anlatımı."
        tags = []
        
        # Dinamik Metadata Okuma (DÜZELTİLDİ: Tags eklendi)
        if os.path.exists('metadata.json'):
            try:
                with open('metadata.json', 'r', encoding='utf-8') as f:
                    m = json.load(f)
                    title = m.get('title', title)
                    description = m.get('description', description)
                    # Tags verisini al (String veya Listeyi destekler)
                    raw_tags = m.get('tags', [])
                    if isinstance(raw_tags, str):
                        tags = [t.strip() for t in raw_tags.split(',')]
                    else:
                        tags = raw_tags
                    print(f"📄 Dinamik Veri Alındı: {title}")
            except Exception as e:
                print(f"⚠️ metadata.json okunamadı, standart başlık kullanılıyor: {e}")

        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags, # ✅ Etiketler YouTube'a gönderiliyor
                'categoryId': '27'
            },
            'status': {
                'privacyStatus': 'unlisted',
                'selfDeclaredMadeForKids': False
            }
        }

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
        print(f"🎉 BAŞARI! Video yüklendi. ID: {video_id}")

        if os.path.exists("s.png"):
            print("🖼️ Kapak fotoğrafı yükleniyor...")
            time.sleep(10)
            try:
                youtube.thumbnails().set(
                    videoId=video_id,
                    media_body=MediaFileUpload("s.png")
                ).execute()
                print("✅ Kapak fotoğrafı başarıyla eklendi.")
            except Exception as thumb_err:
                print(f"⚠️ Kapak hatası: {thumb_err}")

    except Exception as e:
        print(f"❌ KRİTİK SİSTEM HATASI: {e}")

if __name__ == "__main__":
    upload_video()
```

---

## 🎯 Şu An Ne Yapılmalı?

1.  **Kod Güncellemesi:** GitHub'daki `scripts/upload_to_youtube.py` dosyasını açın ve yukarıdaki yeni "Tags Fix" sürümüyle güncelleyin. (Böylece az önce gönderdiğiniz etiketler YouTube'da görünür hale gelecek).
2.  **Run Once:** Her şey 200 OK olduğuna göre, artık fırlatma kolunu çekebilirsiniz.

**Maarif Matematik Notu:** Hocam, o logdaki `200` kodu Maarif Matematik'in "başarı belgesi"dir. Artık teknik engelleri tamamen süpürdük. Tebrikler! 🚀🎓
