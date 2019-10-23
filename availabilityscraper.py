from bs4 import BeautifulSoup
import requests
import json

my_url = 'https://www.apartments.com/off-campus-housing/il/champaign/university-of-illinois-at-urbana-champaign/'
response = requests.get(my_url)
content = BeautifulSoup(response.content, "html.parser")

availabilityArray = []
for availiability in soup.findAll('div', attrs = {"class": "apartmentRentRollupContainer"}):
    availabilityObj = {
    "Time available": availabilityArray.find('span', attrs={"class": "availabilityDisplay noBedSelected"}).text.encode('utf-8')
    }
    availabilityArray.append(availabilityObj)
    print(availabilityObj)

with open('availabilityData.json', 'w') as file:
    json.dump(availabilityArray, file)
    
