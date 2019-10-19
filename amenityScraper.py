from bs4 import BeautifulSoup
import requests
import json

url = 'https://firstcolumnliving.com/properties/512-green/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

amenitiesArr = []
for amenity in content.findAll('div'  , attrs = {"class": "feature-list"}):
    amenityObject = {
        "features": amenity.find('p', attrs={"class": "uppercase"}).text.encode('utf-8')
    }
    print(amenityObject)
    amenitiesArr.append(amenityObject)
print(amenitiesArr)
with open('amenityData.json', 'w') as outfile:
    json.dump(amenitiesArr, outfile)


    
