import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video():
    client_secrets = json.loads(os.environ.get('CLIENT_SECRETS_JSON'))
    token_data = json.loads(os.environ.get('TOKEN_JSON'))
    creds = Credentials.from_authorized_user_info(token_data)
    youtube = build('youtube', 'v3', credentials=creds)

    # --- YENİ YEDEK DEĞERLER (İSİMSİZ VE GÜVENLİ) ---
    video_title = "Birim Kesirler Mantığı | Maarif Matematik"
    video_description = "Maarif Modeli'ne uygun, mantık odaklı matematik dersleri."
    video_tags = ["matematik", "ders", "maarif"]

    # metadata.json DOSYASINI HER YERDE ARA
    possible_paths = ['metadata.json', 'scripts/metadata.json', '../metadata.json']
    metadata_found = False

    for path in possible_paths:
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                    # Hem düz hem nested yapıyı kontrol et
                    t = metadata.get('title') or metadata.get('metadata', {}).get('title')
                    d = metadata.get('description') or metadata.get('metadata', {}).get('description')
                    tg = metadata.get('tags') or metadata.get('metadata', {}).get('tags')

                    if t: video_title = t
                    if d: video_description = d
                    if tg: video_tags = tg
                    metadata_found = True
                    print(f"BAŞARILI: Metadata şurada bulundu: {path}")
                    break
            except:
                continue

    if not metadata_found:
        print("UYARI: metadata.json hiçbir yerde bulunamadı. Güvenli varsayılanlar kullanılıyor.")

    video_file = "media/videos/final_output.mp4"
    if not os.path.exists(video_file):
        print("HATA: Video dosyası bulunamadı!")
        return

    # Yükleme Başlıyor
    request_body = {
        'snippet': {'title': video_title, 'description': video_description, 'tags': video_tags, 'categoryId': '27'},
        'status': {'privacyStatus': 'public', 'selfDeclaredMadeForKids': False}
    }

    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)
    response = youtube.videos().insert(part='snippet,status', body=request_body, media_body=media).execute()
    video_id = response.get('id')
    print(f"Video yüklendi! ID: {video_id}")

    # KAPAK YÜKLEME (s.png)
    if os.path.exists("s.png"):
        time.sleep(10) # YouTube'un videoyu görmesi için bekleme
        try:
            youtube.thumbnails().set(videoId=video_id, media_body=MediaFileUpload("s.png")).execute()
            print("Kapak başarıyla eklendi!")
        except Exception as e:
            print(f"Kapak hatası: {e}")

if __name__ == "__main__":
    upload_video()
