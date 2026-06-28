"""
batch_thumbnail.py
batch_thumbnails.json dosyasindaki tum videolara thumbnail yukler.
Format: [{"video_id": "xxx", "file": "thumbnails/xxx.png"}, ...]
"""
import os, json, base64, time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseUpload
from google.auth.transport.requests import Request
import io

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def youtube_baglan():
    t_json = os.environ.get("TOKEN_JSON")
    if not t_json:
        raise ValueError("TOKEN_JSON yok!")
    creds = Credentials.from_authorized_user_info(json.loads(t_json), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("youtube", "v3", credentials=creds)

def main():
    with open("batch_thumbnails.json", encoding="utf-8") as f:
        items = json.load(f)

    print(f"{len(items)} thumbnail yuklenecek...")
    yt = youtube_baglan()

    for i, item in enumerate(items):
        vid = item["video_id"]
        img_b64 = item.get("image_b64")

        try:
            img_data = base64.b64decode(img_b64)
            media = MediaIoBaseUpload(io.BytesIO(img_data), mimetype="image/png")
            yt.thumbnails().set(videoId=vid, media_body=media).execute()
            print(f"  [{i+1}/{len(items)}] OK: {vid}")
            time.sleep(1)  # API rate limit icin kisa bekleme
        except Exception as e:
            print(f"  [{i+1}/{len(items)}] HATA {vid}: {e}")

    print("Tamamlandi!")

if __name__ == "__main__":
    main()
