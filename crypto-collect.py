import requests
from bs4 import BeautifulSoup
from urls import REQ, CURRENCIES

def getPage(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = (
        soup
        .find('div', attrs={'class': 'priceValue'})
        .find('span')
        .text
    )
    return float(price[1:].replace(',', ''))

if __name__ == '__main__':
    for cur in CURRENCIES:
        url = '/'.join([REQ, cur])
        print(getPage(url))

