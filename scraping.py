
from google_play_scraper import app, reviews_all, Sort
import csv

scrapreview = reviews_all(
    'com.gojek.app',         
    lang='id',             # Bahasa ulasan (default: 'en')
    country='id',          # Negara (default: 'us')
    sort=Sort.MOST_RELEVANT, # Urutan ulasan (default: Sort.MOST_RELEVANT)
)


with open('ulasan_aplikasi_gojek_100k.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review', 'Rating'])  # Menulis header kolom
    for review in scrapreview:
        writer.writerow([review['content'], review['score']])  # Menulis konten ulasan dan rating ke dalam file CSV