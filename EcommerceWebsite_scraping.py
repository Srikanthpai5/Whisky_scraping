import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://www.thewhiskyexchange.com/"

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
           }

# https://www.thewhiskyexchange.com/new-products#id=02362

productlinks = []
for x in range(1,5):
    r = requests.get(f'https://www.thewhiskyexchange.com/c/309/blended-malt-scotch-whisky?pg={x}&psize=24&sort=pasc')

    soup = BeautifulSoup(r.content, 'html.parser')

    productlist = soup.find_all('li', {'class':'product-grid__item'})

    for item in productlist:
        for a in item.find_all('a', href=True):
            productlinks.append(baseurl + a['href'])


print(productlinks)
print()
print("--------------------------")
print(len(productlinks))
print()
print("--------------------------")


# testl = 'https://www.thewhiskyexchange.com/p/38703/highland-harvest-organic-blended-malt-7-casks-half-bottle'

whisky_list = list()

for l in productlinks:
    r = requests.get(l, headers= headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        name = soup.find('h1', {'class':'product-main__name'}).text.strip()
        whisky_type = soup.find('ul', {'class':'product-main__meta'}).text.strip()
        alcohol_range = soup.find('p', {'class':'product-main__data'}).text.strip()
        stock_info = soup.find('p', {'class':'product-action__stock-flag'}).text.strip()
        price = soup.find('p', {'class':'product-action__price'}).text.strip()
        VAT = soup.find('p', {'class':'product-action__vat-price'}).text.strip()[0:6]
        per_litre_info = soup.find('p', {'class':'product-action__unit-price'}).text.strip()[1:-1]
    except:
        pass
    # rating = soup.find('p', {'class':'product-action__unit-price'}).text.strip()
    # not including rating here

    whisky = {
        'name': name, 'whisky_type': whisky_type, 'alcohol_range': alcohol_range,
        'stock_info': stock_info, 'price': price, 'VAT': VAT,
        'per_litre_info': per_litre_info}
    whisky_list.append(whisky)

    if len(whisky_list)%10 == 0:
        print('saved till :', whisky['name'])

# subname = soup.find('span', {'class':'product-main__sub-name'}).text.strip() --- Not needed as top element has been used for scraping
# print(name, whisky_type, alcohol_range, stock_info, price, VAT, per_litre_info)
# print(VAT)

# ----- UNCOMMENT NEXT 2 LINES BEFORE RUN

# df = pd.DataFrame(whisky_list)
# df.to_csv('whiskys.csv')


print(len(whisky_list))