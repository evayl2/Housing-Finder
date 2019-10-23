from bs4 import BeautifulSoup
import requests
import json

my_url = 'https://www.apartments.com/off-campus-housing/il/champaign/university-of-illinois-at-urbana-champaign/'
response = requests.get(my_url)
content = BeautifulSoup(response.content, "html.parser")

priceArray = []
for price in soup.findAll('div', attrs = {"class": "apartmentRentRollupContainer"}):
    priceObj = {
    "Prices": priceArray.find('span', attrs={"class": "altRentDisplay"}).text.encode('utf-8')
    }
    priceArray.append(priceObj)
    print(priceObj)

with open('priceData.json', 'w') as file:
    json.dump(priceArray, file)
    

