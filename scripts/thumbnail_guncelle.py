"""
thumbnail_guncelle.py
GitHub Actions tarafindan calistirilir.

Gerekli secret: TOKEN_JSON
Gerekli dosyalar (repo kokunde):
  thumbnail.png          -- yuklenecek thumbnail
  thumbnail_update.json  -- {"video_id": "xxx"}
"""
import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

SCOPES      = ["https://www.googleapis.com/auth/youtube.force-ssl"]
THUMB_PATH  = "thumbnail.png"
META_PATH   = "thumbnail_update.json"


def youtube_baglan():
    t_json = os.environ.get("TOKEN_JSON")
    if not t_json:
        raise ValueError("TOKEN_JSON secret tanimli degil!")
    creds = Credentials.from_authorized_user_info(json.loads(t_json), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("youtube", "v3", credentials=creds)


def main():
    if not os.path.exists(META_PATH):
        raise FileNotFoundError(f"Metadata bulunamadi: {META_PATH}")
    if not os.path.exists(THUMB_PATH):
        raise FileNotFoundError(f"Thumbnail bulunamadi: {THUMB_PATH}")

    with open(META_PATH, encoding="utf-8") as f:
        m = json.load(f)

    video_id = m.get("video_id")
    if not video_id:
        raise ValueError("thumbnail_update.json icinde video_id bulunamadi!")

    print(f"Video ID  : {video_id}")
    print(f"Thumbnail : {THUMB_PATH}")

    youtube = youtube_baglan()
    youtube.thumbnails().set(
        videoId=video_id,
        media_body=MediaFileUpload(THUMB_PATH)
    ).execute()
    print(f"Thumbnail yuklendi! https://youtu.be/{video_id}")


if __name__ == "__main__":
    main()
