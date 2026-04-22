import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video():
    try:
        t_env = os.environ.get('TOKEN_JSON')
        if not t_env: raise Exception("TOKEN_JSON bulunamadı!")
        
        token_data = json.loads(t_env)
        creds = Credentials.from_authorized_user_info(token_data)
        youtube = build('youtube', 'v3', credentials=creds)

        with open('metadata.json', 'r', encoding='utf-8') as f:
            m = json.loads(f.read(), strict=False) 
            title = m.get('title', 'Maarif Matematik Dersi')
            description = m.get('description', 'Mantık odaklı anlatım.')
            tags = m.get('tags', [])

        body = {
            'snippet': {'title': title, 'description': description, 'tags': tags, 'categoryId': '27'},
            'status': {'privacyStatus': 'unlisted', 'selfDeclaredMadeForKids': False}
        }

        print(f"🚀 Yükleniyor: {title}")
        media = MediaFileUpload("media/videos/final_output.mp4", chunksize=-1, resumable=True)
        response = youtube.videos().insert(part='snippet,status', body=body, media_body=media).execute()
        
        if os.path.exists("s.png"):
            youtube.thumbnails().set(videoId=response.get('id'), media_body=MediaFileUpload("s.png")).execute()
            print("✅ İşlem Başarılı!")

    except Exception as e:
        print(f"❌ HATA: {e}")

if __name__ == "__main__":
    upload_video()
