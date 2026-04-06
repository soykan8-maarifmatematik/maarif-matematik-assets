import os
import json
import glob
import re
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload

def clean_json_string(data):
    """
    GitHub Secrets'tan gelen verideki olası Markdown işaretlerini (```json ... ```) 
    veya hatalı satır sonlarını temizler.
    """
    if not data:
        return None
    
    # Baş ve sondaki boşlukları temizle
    data = data.strip()
    
    # Eğer veri Markdown kod bloğu içindeyse (```json ... ```) temizle
    if data.startswith("```"):
        # Baştaki ```json veya ``` kısmını sil
        data = re.sub(r'^
