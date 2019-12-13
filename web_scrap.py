import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from fileinput import filename
my_url = 'https://www.newegg.com/global/za-en/Gaming-Laptops/SubCategory/ID-3365?Tid=1419157'
#opening connection
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")
page_soup.h1

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "product_name"

f.write(headers)

for container in containers:
    
    brand = container.find(class_='item-title').get_text()

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

print("brand: " + brand)
print("product_name: " + product_name)
print("shipping: " + shipping)

f.write(product_name.replace(",", "|") + "," )

f.close()