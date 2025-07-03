import requests
from bs4 import BeautifulSoup
import math
import csv

querry = input("Enter product to search: ").replace(" ", "+")
count=0
product_list = []
data_range=int(input("How many data you want "))

i=math.ceil(data_range / 20)
for page in range(0, i):

 url=f"https://www.flipkart.com/search?q={querry}&page={page}"

 response=requests.get(url)
 htmlContent=response.content

 soup= BeautifulSoup(htmlContent, 'html.parser')

 product_container= soup.find_all('div',class_='cPHDOP col-12-12')

 for product in product_container:
    title_tag=product.find('div', class_='KzDlHZ')
    price_tag=product.find('div',class_='Nx9bqj _4b5DiR')
    rating_tag=product.find('div',class_='XQDdHH')
    image_tag=product.find('img',class_='DByuf4')

    if title_tag and price_tag:
        title = title_tag.get_text().strip()
        price = price_tag.get_text().strip()
        rating = rating_tag.get_text().strip() if rating_tag else "No rating"
        image=image_tag.get('src').strip()
        count =count+1
        product_list.append({
            's.no':count,
            'category':querry,
            'title': title,
            'price': price.replace('₹', ''),
            'rating': rating,
            'image': image
        })

for item in product_list:
    print(item ,"\n")



with open('flipkart_products2.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['s.no', 'category', 'title', 'price', 'rating', 'image'])
    writer.writeheader()
    writer.writerows(product_list)
