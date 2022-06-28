import requests
from bs4 import BeautifulSoup

def search(query):
    url= 'https://www.expedia.com/Hotel-Search?adults=2&d1=2022-07-07&d2=2022-07-08&destination={query}'
    html=requests.get(url=url)
    html.status_code
    soup=BeautifulSoup(html.text, 'html.parser')
    print(html.text, 'html.parser')
    listing=soup.find_all('div', {'class':'uitk-layout-grid uitk-layout-grid-columns-medium-3'})
    data = {
        'name': listing.find('h2', {'class': "uitk-heading-5"}).text,
        'img' : listing.find('img', {'class':"uitk-image-media"}).text,
        'rating':listing.find('span', {'class':"uitk-text uitk-type-300 uitk-type-bold uitk-text-default-theme"}).text,
        'review':listing.find('span', {'class':"uitk-text uitk-type-300 uitk-text-default-theme"}).text,
        'price': listing.find('div', {'class':"uitk-text uitk-type-600 uitk-type-bold uitk-text-emphasis-theme"}).text,
        'listingdetail': listing.find('a', {'data-stid': 'open-hotel-information'})['href'],
    }
    return(data)


