import requests
from bs4 import BeautifulSoup

def scrape_sweetwater(url):
    response = requests.get(url)

    return response.content