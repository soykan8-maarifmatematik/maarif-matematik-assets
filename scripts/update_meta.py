"""
update_meta.py
GitHub Actions tarafindan calistirilir.

Gerekli secret: TOKEN_JSON
Gerekli dosya: meta_update.json
  {
    "video_id": "xxx",
    "title": "...",          (opsiyonel)
    "description": "...",    (opsiyonel)
    "tags": [...]            (opsiyonel)
  }
"""
import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES    = ["https://www.googleapis.com/auth/youtube.force-ssl"]
META_PATH = "meta_update.json"


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
        raise FileNotFoundError(f"Bulunamadi: {META_PATH}")

    with open(META_PATH, encoding="utf-8") as f:
        m = json.load(f)

    video_id = m.get("video_id")
    if not video_id:
        raise ValueError("meta_update.json icinde video_id yok!")

    youtube = youtube_baglan()

    # Mevcut video bilgilerini al
    resp = youtube.videos().list(part="snippet", id=video_id).execute()
    if not resp.get("items"):
        raise ValueError(f"Video bulunamadi: {video_id}")

    snippet = resp["items"][0]["snippet"]

    # Sadece verilen alanları güncelle
    if "title" in m:
        snippet["title"] = m["title"]
    if "description" in m:
        snippet["description"] = m["description"]
    if "tags" in m:
        snippet["tags"] = m["tags"]

    youtube.videos().update(
        part="snippet",
        body={"id": video_id, "snippet": snippet}
    ).execute()

    print(f"Guncellendi: https://youtu.be/{video_id}")
    print(f"Baslik: {snippet['title']}")


if __name__ == "__main__":
    main()
