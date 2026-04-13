import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# ⚠️ BU ADRESİN SONUNDA BOŞLUK OLMAMALI
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def upload_video():
    try:
        t_json = os.environ.get('TOKEN_JSON')
        cs_json = os.environ.get('CLIENT_SECRETS_JSON')
        
        if not t_json:
            print("❌ HATA: TOKEN_JSON GitHub Secret bulunamadı!")
            return

        # JSON verisini yükle
        token_data = json.loads(t_json)
        
        # 🛡️ YETKİ TAMİRİ: Token içindeki yetkiyi kodla aynı yapmaya zorluyoruz
        token_data['scopes'] = SCOPES 
        
        creds = Credentials.from_authorized_user_info(token_data, SCOPES)
        
        # Anahtarın süresi dolmuşsa yenile
        if creds and creds.expired and creds.refresh_token:
            print("🔄 Anahtar süresi dolmuş, YouTube'dan taze onay alınıyor...")
            creds.refresh(Request())
            
        youtube = build('youtube', 'v3', credentials=creds)
        print("✅ YouTube bağlantısı başarıyla kuruldu.")
        
        # Dosya ve Metadata Ayarları
        video_path = "media/videos/final_output.mp4"
        title = "Birim Kesirler Mantığı | Maarif Matematik"
        
        if os.path.exists('metadata.json'):
            with open('metadata.json', 'r', encoding='utf-8') as f:
                m = json.load(f)
                title = m.get('title', title)

        body = {
            'snippet': {'title': title, 'categoryId': '27'},
            'status': {'privacyStatus': 'public', 'selfDeclaredMadeForKids': False}
        }

        print(f"🚀 Video yükleniyor: {title}")
        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        response = youtube.videos().insert(part='snippet,status', body=body, media_body=media).execute()
        print(f"🎉 BAŞARI! Video YouTube'da yayında. ID: {response.get('id')}")

    except Exception as e:
        print(f"❌ KRİTİK HATA: {e}")
        print("İpucu: Eğer 'invalid_scope' diyorsa, lütfen anahtar.py ile yeni kod alırken kutucuğu işaretleyin.")

if __name__ == "__main__":
    upload_video()
