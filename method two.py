import requests
from bs4 import BeautifulSoup
import pandas as pd

def search(query):
    url = requests.get('https://www.expedia.com/Hotel-Search?adults=2&d1=2022-07-07&d2=2022-07-08&destination={query}')
    html=requests.get(url=url)
    bsObj = BeautifulSoup(html, 'html.parser')
    print(html.text, 'html.parser')
    hotel = []
    for name in bsObj.findAll('h2',{'class':'uitk-heading-5'}):
        hotel.append(name.text.strip())
    ratings = []
    for rating in bsObj.findAll('span',{'class':'uitk-text uitk-type-300 uitk-type-bold uitk-text-default-theme'}):
        ratings.append(rating['alt'])
    reviews = []
    for reviews in bsObj.findAll('span',{'class':'uitk-text uitk-type-300 uitk-text-default-theme'}):
        reviews.append(reviews.text.strip())
    images = []
    for images in bsObj.findAll('img',{'class':'uitk-image-media'}):
        images.append(images.text.strip())
    listingdetail = []
    for review in bsObj.findAll('a',{'class':'open-hotel-information'}):
        listingdetail.append(listingdetail.text.strip())['href']
    price = []
    for p in bsObj.findAll('div',{'class':'uitk-text uitk-type-600 uitk-type-bold uitk-text-emphasis-theme'}):
        price.append(p.text.replace('₹','').strip()) 
    price[:5]

    d1 = {
    'Hotel':hotel,
    'Ratings':ratings,
    'No_of_Reviews':reviews,
    'Price':price,
    'images':images,
    'link':listingdetail
    }
    df = pd.DataFrame.from_dict(d1)