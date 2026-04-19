import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video():
    try:
        # 1. Kimlik Doğrulama
        t_env = os.environ.get('TOKEN_JSON')
        if not t_env: raise Exception("TOKEN_JSON bulunamadı!")
        token_data = json.loads(t_env)
        creds = Credentials.from_authorized_user_info(token_data)
        youtube = build('youtube', 'v3', credentials=creds)

        # 2. Metadata Okuma
        if not os.path.exists('metadata.json'):
            raise Exception("metadata.json dosyası bulunamadı!")
            
        with open('metadata.json', 'r', encoding='utf-8') as f:
            m = json.load(f)
            title = m.get('title', 'Başlık Alınamadı')
            description = m.get('description', 'Açıklama Alınamadı')
            tags = m.get('tags', [])

        # 3. Video Yükleme
        video_path = "media/videos/final_output.mp4"
        body = {
            'snippet': {'title': title, 'description': description, 'tags': tags, 'categoryId': '27'},
            'status': {'privacyStatus': 'unlisted', 'selfDeclaredMadeForKids': False}
        }

        print(f"🚀 Yükleniyor: {title}")
        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        response = youtube.videos().insert(part='snippet,status', body=body, media_body=media).execute()
        
        if os.path.exists("s.png"):
            youtube.thumbnails().set(videoId=response.get('id'), media_body=MediaFileUpload("s.png")).execute()
            print("✅ Kapak ve SEO başarıyla tamamlandı.")

    except Exception as e:
        print(f"❌ SİSTEM DURDURULDU: {e}")

if __name__ == "__main__":
    upload_video()
