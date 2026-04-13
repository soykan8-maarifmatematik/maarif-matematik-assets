🔐 Kusursuz Yetki SenkronizasyonuHocam, bu iki dosya arasındaki yetki (Scope) tanımını "mıhladım". İkisini de aynı anda güncellediğimizde sistem çalışacak.1. GitHub'a Yapıştırılacak Kod (scripts/upload_to_youtube.py)import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# ⚠️ KRİTİK: Bu adres anahtar.py ile milimetrik aynı olmalı
SCOPES = ['[https://www.googleapis.com/auth/youtube.force-ssl](https://www.googleapis.com/auth/youtube.force-ssl)']

def upload_video():
    try:
        t_json = os.environ.get('TOKEN_JSON')
        cs_json = os.environ.get('CLIENT_SECRETS_JSON')
        
        if not t_json: raise Exception("TOKEN_JSON eksik!")
        
        token_data = json.loads(t_json)
        # Token içindeki eski yetkileri temizleyip bizimkini dayatıyoruz
        token_data['scopes'] = SCOPES 
        
        creds = Credentials.from_authorized_user_info(token_data, SCOPES)
        
        if creds and creds.expired and creds.refresh_token:
            print("🔄 Anahtar tazeleniyor...")
            creds.refresh(Request())
            
        youtube = build('youtube', 'v3', credentials=creds)
        print("✅ YouTube kapısı açıldı!")
        
        # Video Yükleme Ayarları
        video_path = "media/videos/final_output.mp4"
        metadata_path = "metadata.json"
        
        title = "Birim Kesirler Mantığı | Maarif Matematik"
        if os.path.exists(metadata_path):
            with open(metadata_path, 'r', encoding='utf-8') as f:
                m = json.load(f)
                title = m.get('title', title)

        body = {
            'snippet': {'title': title, 'categoryId': '27'},
            'status': {'privacyStatus': 'public', 'selfDeclaredMadeForKids': False}
        }

        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        response = youtube.videos().insert(part='snippet,status', body=body, media_body=media).execute()
        print(f"🚀 YAYINDA! ID: {response.get('id')}")

    except Exception as e:
        print(f"❌ HATA: {e}")

if __name__ == "__main__":
    upload_video()
2. Bilgisayarda Çalıştırılacak Kod (anahtar.py)import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow

# ⚠️ KRİTİK: Yukarıdakiyle birebir aynı adres
SCOPES = ['[https://www.googleapis.com/auth/youtube.force-ssl](https://www.googleapis.com/auth/youtube.force-ssl)']

def get_token():
    client_file = 'client_secret.json' # Masaüstü istemcisi dosyası
    flow = InstalledAppFlow.from_client_secrets_file(client_file, SCOPES)
    creds = flow.run_local_server(port=0)
    
    print("\n--- GITHUB TOKEN_JSON İÇİN KOPYALA ---\n")
    print(creds.to_json())
    print("\n--------------------------------------\n")

if __name__ == "__main__":
    get_token()
