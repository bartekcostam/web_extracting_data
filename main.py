import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# URL strony z listą podstron zawierających pliki PDF
url = 'https://arkusze.pl/informatyka-matura-poziom-rozszerzony/'

# Katalog główny do zapisywania pobranych plików
main_download_dir = 'matura_pdfs'
os.makedirs(main_download_dir, exist_ok=True)

# Pobieranie strony i parsowanie HTML
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Znalezienie wszystkich linków do podstron z plikami PDF
page_links = soup.find_all('a', href=True)
page_links = [link['href'] for link in page_links if link['href']]

# Funkcja do pobierania plików PDF z podstrony
def download_pdfs_from_page(page_url, subfolder):
    page_response = requests.get(page_url)
    page_soup = BeautifulSoup(page_response.content, 'html.parser')
    pdf_links = page_soup.find_all('a', href=True)
    pdf_links = [link['href'] for link in pdf_links if link['href'].endswith('.pdf') or link['href'].endswith('.zip')]

    for pdf_link in pdf_links:
        pdf_url = urljoin(page_url, pdf_link)
        pdf_response = requests.get(pdf_url)
        pdf_name = os.path.join(subfolder, pdf_url.split('/')[-1])

        with open(pdf_name, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)

        print(f'Pobrano: {pdf_name}')

# Przetwarzanie każdej podstrony i pobieranie plików PDF
for link in page_links:
    page_url = urljoin(url, link)
    page_name = link.split('/')[-1].replace('.html', '')
    subfolder = os.path.join(main_download_dir, page_name)
    os.makedirs(subfolder, exist_ok=True)
    download_pdfs_from_page(page_url, subfolder)
