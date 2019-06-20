import requests
import re
from bs4 import BeautifulSoup

def get_params(o):
    params = o.find('ul', class_='teaser__params')
    if params:
        return [p.string.strip() for p in params.find_all("li")]


def get_image_src(o):
    if o.img:
        src1 = o.img.get('src')
        src2 = o.img.get('data-src')
        return src1 or src2

def get_price(o):
    price = o.find('p', class_=re.compile(".*__price")).string or ''
    return price.strip()


def get_title(o):
    title = o.find("a", class_=re.compile(".*__anchor")).string.strip() or ''
    return title.strip()


def get_gratka_offers(price_max):

    resp = requests.get(f"https://gratka.pl/nieruchomosci/wroclaw/wynajem/q/wroc%C5%82aw-mieszkanie?cena-calkowita:max={price_max}&powierzchnia-w-m2:min=60&lokalizacja_szerokosc-geograficzna-y=51.113805&lokalizacja_dlugosc-geograficzna-x=17.041177&lokalizacja_region=dolnoslaskie")

    c = resp.content
    soup = BeautifulSoup(c, "html.parser")

    offers = soup.find_all("article", id=re.compile("offer-*"))

    return [{
            'link': o['data-href'],
            'title': get_title(o),
            'price': get_price(o),
            'img': get_image_src(o),
            'params': get_params(o),
    } for o in offers ]

if __name__ == "__main__":
    print(get_gratka_offers(2500))


