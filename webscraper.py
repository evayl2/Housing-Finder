from bs4 import BeautifulSoup
import requests
import json

my_url = https://www.apartments.com/907-third-champaign-il/50v7g2q/
response = requests.get(my_url)
soup = BeautifulSoup(response.text, “html.parser”)

amenities = []
for amenity in soup.findAll('div', attrs = {"class": "feature-list"}):
    amenityObj = {
    "features": amenity.find('p', attrs={"class": "uppercase"}).text.encode('utf-8')
    }
    amenities.append(ammenityObj)
    print(ammenityObj)

with open('amenityData.json', 'w') as file:
    json.dump(amenities, file)
