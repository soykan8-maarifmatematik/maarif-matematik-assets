import os
import json
import glob
import re
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload

def clean_json_string(data):
    if not data:
        return None
    # Markdown kod bloklarını (```json ... ```) temizle
    data = data.strip()
    if data.startswith("```"):
        data = re.sub(r'^
http://googleusercontent.com/immersive_entry_chip/1

Hocam, hatanın sebebi scriptin JSON'u okumaya başlarken hiçbir karakter bulamamasıydı. Yukarıdaki yeni Python kodu (`scripts/upload_to_youtube.py`) veriyi okumadan önce temizlik yapacak şekilde tasarlandı. 

**Şimdi ne yapmalısın?**
1. Canvas'taki yeni Python kodunu kopyala ve GitHub'daki `scripts/upload_to_youtube.py` dosyasını güncelle.
2. GitHub'da `Actions` sekmesine gidip tekrar dene. 

Eğer her şey yolundaysa, bu sefer JSON hatası yerine "YouTube'a yükleme başlıyor..." yazısını göreceğiz. Bekliyorum! 🌿🔢✨
