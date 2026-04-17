import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# ⚠️ YETKİ KAPSAMI - TERTEMİZ URL (Boşluksuz ve Köşeli Parantezsiz)
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def upload_video():
    try:
        t_json = os.environ.get('TOKEN_JSON')
        if not t_json:
            print("❌ HATA: TOKEN_JSON bulunamadı!")
            return

        token_data = json.loads(t_json)
        # Token içindeki yetkileri kod seviyesinde garantiye alıyoruz
        token_data['scopes'] = SCOPES 
        creds = Credentials.from_authorized_user_info(token_data, SCOPES)
        
        if creds and creds.expired and creds.refresh_token:
            print("🔄 Erişim anahtarı yenileniyor...")
            creds.refresh(Request())
            
        youtube = build('youtube', 'v3', credentials=creds)
        print("✅ YouTube API bağlantısı başarıyla kuruldu.")
        
        # Varsayılan Değerler
        video_path = "media/videos/final_output.mp4"
        title = "İbrahim Soykan | Maarif Matematik - Yeni Ders"
        description = "Mantık odaklı, ezbersiz matematik anlatımı."
        tags = []
        
        # Dinamik Metadata Okuma (Tags ve SEO Verileri)
        if os.path.exists('metadata.json'):
            try:
                with open('metadata.json', 'r', encoding='utf-8') as f:
                    m = json.load(f)
                    title = m.get('title', title)
                    description = m.get('description', description)
                    # Tags verisini hem liste hem string formatında destekler
                    raw_tags = m.get('tags', [])
                    if isinstance(raw_tags, list):
                        tags = raw_tags
                    else:
                        tags = [t.strip() for t in str(raw_tags).split(',')]
                    print(f"📄 Metadata başarıyla işlendi: {title}")
            except Exception as e:
                print(f"⚠️ metadata.json okunamadı, standart başlık kullanılıyor: {e}")

        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags,
                'categoryId': '27' # Eğitim Kategorisi
            },
            'status': {
                'privacyStatus': 'unlisted', # Siz hazır olunca public yaparsınız
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
        print(f"🎉 BAŞARI! Video yüklendi. Video ID: {video_id}")

        # Kapak Fotoğrafı Mıhlama (s.png)
        if os.path.exists("s.png"):
            print("🖼️ Kapak fotoğrafı yükleniyor...")
            time.sleep(10) # YouTube'un videoyu işlemesi için kısa bekleme
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
