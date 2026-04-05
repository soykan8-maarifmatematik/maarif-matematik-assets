import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.http
import pickle

def upload_video():
    # Token yukleme
    with open('token.pickle', 'rb') as token:
        credentials = pickle.load(token)

    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "categoryId": "27", # Education
                "description": "Maarif Matematik - Mantik Temelli Egitim",
                "title": "Maarif Matematik - Yeni Ders (Kontrol Ediniz)",
                "tags": ["matematik", "maarif", "egitim"]
            },
            "status": {
                "privacyStatus": "unlisted", # BURASI KRITIK: Videoyu kimse gormez.
                "selfDeclaredMadeForKids": True # Cocuklara ozel icerik ayari
            }
        },
        media_body=googleapiclient.http.MediaFileUpload("media/videos/lesson_code/480p15/LessonScene.mp4")
    )
    response = request.execute()
    print(f"Video yuklendi! ID: {response['id']}")

if __name__ == "__main__":
    upload_video()
