"""
upload_to_youtube.py
GitHub Actions tarafindan calistirilir.

Gerekli secret: TOKEN_JSON
Gerekli dosyalar (repo kokunde):
  current_video.mp4   — yuklenecek video
  metadata.json       — baslik, aciklama, etiketler, publish_at
  s.png               — kapak fotografi (opsiyonel)
"""
import os
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

SCOPES     = ["https://www.googleapis.com/auth/youtube.force-ssl"]
VIDEO_PATH = "current_video.mp4"
THUMB_PATH = "s.png"
META_PATH  = "metadata.json"


def youtube_baglan():
    t_json = os.environ.get("TOKEN_JSON")
    if not t_json:
        raise ValueError("TOKEN_JSON secret tanimli degil!")
    creds = Credentials.from_authorized_user_info(json.loads(t_json), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("youtube", "v3", credentials=creds)


def yukle():
    # Dosya kontrolleri
    if not os.path.exists(VIDEO_PATH):
        raise FileNotFoundError(f"Video bulunamadi: {VIDEO_PATH}")
    if not os.path.exists(META_PATH):
        raise FileNotFoundError(f"Metadata bulunamadi: {META_PATH}")

    with open(META_PATH, encoding="utf-8") as f:
        m = json.load(f)

    # Eski ve yeni format destegi
    title       = m.get("youtube_title") or m.get("title", "Maarif Matematik")
    description = m.get("description", "")
    tags        = m.get("tags", [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",")]
    comment     = m.get("ilk_yorum") or m.get("first_comment", "")
    publish_at  = m.get("publish_at", "")   # "2026-09-07T13:00:00Z"
    playlist_id = m.get("playlist_id", "")  # YouTube oynatma listesi ID

    print(f"Yukleniyor : {title}")
    print(f"Video boyut: {os.path.getsize(VIDEO_PATH) / 1e6:.1f} MB")
    if publish_at:
        print(f"Yayin tarihi: {publish_at}")

    youtube = youtube_baglan()

    # Video metadata
    body = {
        "snippet": {
            "title":       title,
            "description": description,
            "tags":        tags,
            "categoryId":  "27",   # Education
        },
        "status": {
            "privacyStatus":           "private",
            "selfDeclaredMadeForKids": False,
        },
    }
    # publishAt varsa YouTube zamaninda otomatik public yapar
    if publish_at:
        body["status"]["publishAt"] = publish_at

    # Video yukle
    media    = MediaFileUpload(VIDEO_PATH, chunksize=-1, resumable=True)
    response = youtube.videos().insert(
        part="snippet,status", body=body, media_body=media
    ).execute()
    video_id = response.get("id")
    print(f"Yuklendi! Video ID: {video_id}")
    print(f"Link: https://youtu.be/{video_id}")

    # Kapak fotografi
    if os.path.exists(THUMB_PATH) and video_id:
        time.sleep(5)
        try:
            youtube.thumbnails().set(
                videoId=video_id,
                media_body=MediaFileUpload(THUMB_PATH)
            ).execute()
            print("Kapak fotografi eklendi.")
        except Exception as e:
            print(f"Kapak yuklenemedi: {e}")

    # Oynatma listesine ekle
    if playlist_id and video_id:
        try:
            youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_id,
                        "resourceId": {
                            "kind":    "youtube#video",
                            "videoId": video_id,
                        },
                    }
                },
            ).execute()
            print(f"Oynatma listesine eklendi: {playlist_id}")
        except Exception as e:
            print(f"Oynatma listesine eklenemedi: {e}")

    # Ilk yorum
    if comment and video_id:
        try:
            youtube.commentThreads().insert(
                part="snippet",
                body={
                    "snippet": {
                        "videoId": video_id,
                        "topLevelComment": {
                            "snippet": {"textOriginal": comment}
                        },
                    }
                },
            ).execute()
            print("Ilk yorum eklendi.")
        except Exception as e:
            print(f"Yorum eklenemedi: {e}")

    return video_id


if __name__ == "__main__":
    vid = yukle()
    print(f"\nTamamlandi. Video ID: {vid}")
