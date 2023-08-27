import requests
from bs4 import BeautifulSoup

def scrape_guitarcenter(url):
    response = requests.get(url)

    return response.content