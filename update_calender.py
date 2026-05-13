import os
import django
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Django ayarlarını yükle
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_campus.settings')
django.setup()

from core.models import AcademicCalendar

def fetch_yeditepe_calendar():
    url = "https://yeditepe.edu.tr/tr/ogrenci/akademik-takvim"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Not: Üniversite sitesindeki tablo yapısına göre burası güncellenmelidir.
    # Şimdilik manuel veri eklemek veya bu scripti tablo yapısına göre özelleştirmek en sağlıklısıdır.
    print("Yeditepe takvim sayfası tarandı. Veri yapısı kontrol ediliyor...")

# Şimdilik en hızlısı Admin'den girmek veya şu komutu terminalde çalıştırmak:
# python manage.py shell