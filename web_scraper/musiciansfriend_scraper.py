import requests
from bs4 import BeautifulSoup
import sys

def scrape_musiciansfriend(url):
    response = requests.get(url)

    html = BeautifulSoup(response.content, 'html5lib')

    vendor = "Musician's Friend"

    names = []
    links = []
    names_links_html = html.find_all("a", class_="ui-link")
    for entry in names_links_html:
        if entry.get_text() != "Details":
            names.append(entry.get_text()) 
        links.append(entry["href"])

    prices = []
    prices_html = html.find_all("span", class_="sale-price")
    for entry in prices_html:
        prices.append(entry.text)


    response = []
    for i in range(0, len(names)):
        response.append({
            "name": names[i],
            "link": "https://www.musiciansfriend.com" + links[i],
            "price": prices[i],
            # This is a dummy image while I figure out how to source the real images
            'image_src': "@/assets/images/logo.png"
        })

    return response

if __name__ == "__main__":
    url = sys.argv[1]
    result = scrape_musiciansfriend(url)
    print(result)