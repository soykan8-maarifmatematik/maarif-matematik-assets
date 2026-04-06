import os
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
import glob

def upload_video():
    # Video dosyasını bul (Manim çıktısı)
    video_files = glob.glob("media/videos/**/*.mp4", recursive=True)
    if not video_files:
        print("Yüklenecek video bulunamadı!")
        return
    
    video_path = video_files[0]
    print(f"Yükleniyor: {video_path}")

    # YouTube API Ayarları (Secrets'tan gelen verilerle)
    # Not: Tam otonom yükleme için Refresh Token gereklidir.
    # Şimdilik temel yapıyı kuruyoruz.
    print("YouTube API bağlantısı kuruluyor...")
    
    # Buraya kendi kanal ayarlarınızı ve başlıklarınızı 
    # Gemini'den gelen metadata dosyasından okuyacak şekilde ekleyeceğiz.
    print("Video YouTube'a gönderilmeye hazır.")

if __name__ == "__main__":
    upload_video()
