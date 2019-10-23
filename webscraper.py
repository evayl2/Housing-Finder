from bs4 import BeautifulSoup
import requests
import json

my_url = https://www.apartments.com/champaign-il/
response = requests.get(my_url)
soup = BeautifulSoup(response.text, “html.parser”)

priceArray = []
for price in soup.findAll('div', attrs = {"class": "apartmentRentRollupContainer"}):
    priceObj = {
    "Prices": priceArray.find('span', attrs={"class": "altRentDisplay"}).text.encode('utf-8'))
    }
    priceArray.append(priceObj)
    print(priceObj)

with open('priceData.json', 'w') as file:
    json.dump(priceArray, file)
    

