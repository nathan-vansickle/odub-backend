import requests
from bs4 import BeautifulSoup
import sys

def scrape_guitarcenter(url):
    response = requests.get(url)

    html = BeautifulSoup(response.content, 'html5lib')

    vendor = 'GuitarCenter'

    names = []
    links = []
    names_links_html = html.find_all("a", class_="jsx-2420341498 product-name gc-font-light font-normal text-base leading-[18px] md:leading-6 text-[#2d2d2d] mb-2 md:h-[72px] h-[36px] hover:underline")
    for entry in names_links_html:
        names.append(entry.get_text())
        links.append(entry['href'])

    prices = []
    prices_html = html.find_all("span", class_="jsx-2420341498 sale-price gc-font-bold text-[#2d2d2d]")
    for price in prices_html:
        prices.append(price.get_text())

    # image_srcs = []
    # images_divs = html.find_all("div", class_="jsx-406435821 plp-product-gallery w-[128px] md:w-auto")
    # for div in images_divs:
    #     img_element = div.find('img')
    #     if img_element:
    #         image_srcs.append(img_element['src'])
        
    response = []
    for i in range(len(names)):
        response.append({
            'name': names[i], 
            'price': prices[i], 
            'link': 'https://guitarcenter.com' + links[i],
            # This is a dummy image while I figure out how to source the real images
            'image_src': "@/assets/images/logo.png"
            })

    return response

if __name__ == '__main__':
    url = sys.argv[1]
    result = scrape_guitarcenter(url)
    print(result)
