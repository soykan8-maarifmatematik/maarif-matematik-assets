"""
playlist_sirala.py
Bir video'yu playlist'te belirli bir video'nun hemen peşine taşır.

Kullanım:
  python araclar/playlist_sirala.py <playlist_id> <video_id> <onceki_video_id>

Örnek:
  python araclar/playlist_sirala.py PLBC68wtjIKHZOqfxtX7wo7E5e0j51V6A1 yeniVideoID auGDIdrxfuE
"""
import os, sys, json, time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def yt_baglan():
    creds = Credentials.from_authorized_user_info(
        json.loads(os.environ["TOKEN_JSON"]), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("youtube", "v3", credentials=creds)


def playlist_items_al(yt, playlist_id):
    items, token = [], None
    while True:
        resp = yt.playlistItems().list(
            part="snippet", playlistId=playlist_id,
            maxResults=50, pageToken=token
        ).execute()
        items.extend(resp["items"])
        token = resp.get("nextPageToken")
        if not token:
            break
    return items


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)

    playlist_id   = sys.argv[1]
    video_id      = sys.argv[2]   # taşınacak video
    onceki_vid_id = sys.argv[3]   # bu videonun hemen peşine koy

    yt = yt_baglan()
    items = playlist_items_al(yt, playlist_id)

    # onceki_vid_id'nin pozisyonunu bul
    onceki_pos = None
    hedef_item_id = None
    for item in items:
        vid = item["snippet"]["resourceId"]["videoId"]
        pos = item["snippet"]["position"]
        if vid == onceki_vid_id:
            onceki_pos = pos
        if vid == video_id:
            hedef_item_id = item["id"]

    if onceki_pos is None:
        print(f"HATA: önceki video bulunamadı: {onceki_vid_id}")
        sys.exit(1)
    if hedef_item_id is None:
        print(f"HATA: taşınacak video playlist'te yok: {video_id}")
        sys.exit(1)

    yeni_pos = onceki_pos + 1
    print(f"'{onceki_vid_id}' → pozisyon {onceki_pos}")
    print(f"'{video_id}' → yeni pozisyon {yeni_pos}")

    yt.playlistItems().update(
        part="snippet",
        body={
            "id": hedef_item_id,
            "snippet": {
                "playlistId": playlist_id,
                "position": yeni_pos,
                "resourceId": {"kind": "youtube#video", "videoId": video_id}
            }
        }
    ).execute()

    print("Tamamlandı!")


if __name__ == "__main__":
    main()
