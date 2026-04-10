import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video():
    # Kimlik Bilgilerini Yükle
    try:
        client_secrets = json.loads(os.environ.get('CLIENT_SECRETS_JSON'))
        token_data = json.loads(os.environ.get('TOKEN_JSON'))
        creds = Credentials.from_authorized_user_info(token_data)
        youtube = build('youtube', 'v3', credentials=creds)
    except Exception as e:
        print(f"HATA: Yetkilendirme başarısız: {e}")
        return

    # --- VARSAYILAN DEĞERLER (Yedek) ---
    video_title = "Birim Kesirler Mantığı | Maarif Matematik"
    video_description = "Maarif Modeli'ne uygun, mantık odaklı matematik dersleri."
    video_tags = ["matematik", "ders", "maarif"]

    # --- METADATA BULUCU (MUTLAK YOL) ---
    # Script scripts/ içinde olduğu için bir üst klasöre (root) bakıyoruz
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    metadata_path = os.path.join(root_dir, 'metadata.json')

    print(f"BİLGİ: Dosya şu adreste aranıyor: {metadata_path}")

    if os.path.exists(metadata_path):
        try:
            with open(metadata_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                # Make.com'dan gelen nested (iç içe) yapıyı destekler
                m = metadata.get('metadata', metadata) 
                video_title = m.get('title', video_title)
                video_description = m.get('description', video_description)
                video_tags = m.get('tags', video_tags)
                print(f"✅ BAŞARILI: {metadata_path} okundu. Başlık: {video_title}")
        except Exception as e:
            print(f"⚠️ Dosya bulundu ama okunamadı: {e}")
    else:
        print(f"❌ HATA: {metadata_path} bulunamadı! Mevcut dosyalar: {os.listdir(root_dir)}")

    # Video Dosyası Kontrolü
    video_file = os.path.join(root_dir, "media/videos/final_output.mp4")
    if not os.path.exists(video_file):
        print(f"HATA: Video bulunamadı: {video_file}")
        return

    # Yükleme Başlıyor
    request_body = {
        'snippet': {'title': video_title, 'description': video_description, 'tags': video_tags, 'categoryId': '27'},
        'status': {'privacyStatus': 'public', 'selfDeclaredMadeForKids': False}
    }

    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)
    response = youtube.videos().insert(part='snippet,status', body=request_body, media_body=media).execute()
    video_id = response.get('id')
    print(f"🎉 VİDEO YÜKLENDİ! ID: {video_id}")

    # Kapak (s.png)
    thumbnail = os.path.join(root_dir, "s.png")
    if os.path.exists(thumbnail):
        time.sleep(15) # YouTube'un videoyu işlemesi için bekle
        try:
            youtube.thumbnails().set(videoId=video_id, media_body=MediaFileUpload(thumbnail)).execute()
            print("✅ Kapak eklendi!")
        except: print("⚠️ Kapak eklenemedi.")

if __name__ == "__main__":
    upload_video()
