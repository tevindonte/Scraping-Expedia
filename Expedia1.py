import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from csv import writer
from datetime import datetime
import os
import sys

executableapp = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

url= 'https://www.expedia.com/Hotel-Search?adults=2&d1=2022-07-07&d2=2022-07-08&destination=Jamaica'
html=requests.get(url=url)
html.status_code
soup=BeautifulSoup(html.text, 'html.parser')
tagchecker=(html.text, 'html.parser')
print(tagchecker)

with open('Expedia{month_day_year}.csv', 'w', encoding='utf8', newline='') as f:
    thewriter=writer(f)
    header = ['hotel', 'ratings', 'reviews', 'images', 'listingdetail', 'price']
    thewriter.writerow(header)

    hotel = []
    for name in soup.findAll('h2',{'class':'uitk-heading-5'}):
        hotel.append(name.text.strip())

    ratings = []
    for rating in soup.findAll('span',{'class':'uitk-text uitk-type-300 uitk-type-bold uitk-text-default-theme'}):
        ratings.append(rating.text.strip())

    reviews = []
    for review in soup.findAll('span',{'class':'uitk-spacing uitk-spacing-padding-inlineend-one'}):
        reviews.append(review.text.strip())

    images = []
    for image in soup.findAll('img',{'class':'uitk-image-media'}):
        images.append(image.attrs['src'])

    listingdetail = []
    linker='https://www.expedia.com/'
    for detail in soup.findAll('a',{'class':'uitk-card-link'}):
        listingdetail.append(detail.get('href'))

    price = []
    for pr in soup.findAll('div',{'class':'uitk-text uitk-type-600 uitk-type-bold uitk-text-emphasis-theme'}):
        price.append(pr.text)
    price[:5]
    info = [hotel, ratings, reviews, images, listingdetail, price]
    thewriter.writerow(info)
    final_path = os.path.join(executableapp)

    d1 = {
    'Hotel':hotel,
    'Ratings':ratings,
    'No_of_Reviews':reviews,
    'Price':price,
    'images':images,
    'link':listingdetail
    }
    df = pd.DataFrame.from_dict(d1)







