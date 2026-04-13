import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# ⚠️ DİKKAT: Sadece tırnak içindeki adresi kullanın, link formatı olmamalı!
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def upload_video():
    try:
        t_json = os.environ.get('TOKEN_JSON')
        cs_json = os.environ.get('CLIENT_SECRETS_JSON')
        
        if not t_json or not cs_json:
            print("❌ HATA: Secrets verileri eksik!")
            return

        token_data = json.loads(t_json)
        # Eğer token içinde eski/yanlış scope kalmışsa temizleyip doğrusunu yazıyoruz
        token_data['scopes'] = SCOPES 
        
        creds = Credentials.from_authorized_user_info(token_data, SCOPES)
        
        if creds and creds.expired and creds.refresh_token:
            print("🔄 Anahtar tazeleniyor...")
            creds.refresh(Request())
            
        youtube = build('youtube', 'v3', credentials=creds)
        print("✅ YouTube bağlantısı kuruldu.")
        
        # Video ve Metadata Kontrolü
        video_path = "media/videos/final_output.mp4"
        if not os.path.exists(video_path):
            print("❌ HATA: Video dosyası bulunamadı!")
            return

        title = "Birim Kesirler Mantığı | Maarif Matematik"
        if os.path.exists('metadata.json'):
            with open('metadata.json', 'r', encoding='utf-8') as f:
                m = json.load(f)
                title = m.get('title', title)

        body = {
            'snippet': {'title': title, 'categoryId': '27'},
            'status': {'privacyStatus': 'public', 'selfDeclaredMadeForKids': False}
        }

        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        response = youtube.videos().insert(part='snippet,status', body=body, media_body=media).execute()
        print(f"🚀 BAŞARI: Video yüklendi! ID: {response.get('id')}")

    except Exception as e:
        print(f"❌ TEKNİK HATA: {e}")

if __name__ == "__main__":
    upload_video()
