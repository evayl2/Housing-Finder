from bs4 import BeautifulSoup
import requests
import json
import numpy as np

def get_random_ua():
    random_ua = ''
    ua_file = 'ua_file.txt'
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_proxy = lines[int(idx)]
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return random_ua

user_agent = get_random_ua()
headers = {
    'user-agent': user_agent,
    }
url = 'https://www.apartments.com/off-campus-housing/il/champaign/university-of-illinois-at-urbana-champaign/?bb=t-lzw3l8rJ3346sK'
response = requests.get(url, headers=headers)
content = BeautifulSoup(response.content, "html.parser")

nameAddressPropertyArr = []
for location in content.findAll('header', attrs = {"class": "placardHeader"}):
    nameAddressPropertyObject = {
        "names": (location.find('a', {"class": ['placardTitle', 'js-placardTitle']})).get('title'),
        "addresses": (location.find('div', attrs={"class": "location"})).get('title'),
        "propertyGroup": (location.find('img', attrs={"class": "propertyLogo"})).get('alt'),
    }
    print(nameAddressPropertyObject)
    nameAddressPropertyArr.append(nameAddressPropertyObject)
    
for info in content.findAll('section', attrs = {"class": "placardContent"}):
    priceBedAvailObject = {
        "price": (info.find('span', {"class": ['altRentDisplay']}).text),
        "beds": (info.find('span', {"class": ['unitLabel']}).text),
        "availability": (info.find('span', {"class": ['availabilityDisplay', 'noBedSelected']}).text),
    }
    print(priceBedAvailObject)
    nameAddressPropertyArr.append(priceBedAvailObject)
    
print(nameAddressPropertyArr)
with open('nameAddressPropertyData.json', 'w') as outfile:
    json.dump(nameAddressPropertyArr, outfile)