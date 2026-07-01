"""
batch_meta.py
batch_meta.json dosyasindaki tum videolara baslik/aciklama/etiket yukler.
Format: [{"video_id":"xxx","title":"...","description":"...","tags":[...]}]
"""
import os, json, time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def youtube_baglan():
    creds = Credentials.from_authorized_user_info(
        json.loads(os.environ["TOKEN_JSON"]), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("youtube", "v3", credentials=creds)

def main():
    with open("batch_meta.json", encoding="utf-8") as f:
        items = json.load(f)

    yt = youtube_baglan()
    print(f"{len(items)} video guncellenecek...")

    for i, item in enumerate(items):
        vid = item["video_id"]
        try:
            yt.videos().update(
                part="snippet",
                body={
                    "id": vid,
                    "snippet": {
                        "title": item["title"],
                        "description": item["description"],
                        "tags": item["tags"],
                        "categoryId": "27"
                    }
                }
            ).execute()
            print(f"  [{i+1}/{len(items)}] OK: {vid}  —  {item['title'][:60]}")
            time.sleep(1)
        except Exception as e:
            print(f"  [{i+1}/{len(items)}] HATA {vid}: {e}")

    print("Tamamlandi!")

if __name__ == "__main__":
    main()
