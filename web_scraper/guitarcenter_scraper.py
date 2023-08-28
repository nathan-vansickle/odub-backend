import requests
from bs4 import BeautifulSoup
import sys

def scrape_guitarcenter(url):
    response = requests.get(url)

    html = BeautifulSoup(response.content, 'html5lib')

    print(html.prettify())

if __name__ == '__main__':
    url = sys.argv[1]
    scrape_guitarcenter(url)