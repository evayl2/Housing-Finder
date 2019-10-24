import json

def filter_list(beds, baths, maxprice, apartment_dict):
    data = []
    for d in apartment_dict['Apartment']:
        if (beds is not None) and (d['beds'] == beds):
            print(5)
            data.append(d)
        elif (baths is not None) and (d['baths'] == baths):
            print(0)
            data.append(d)
        elif (maxprice is not None) and (d['price'] <= maxprice):
            print(3)
            data.append(d)
    return data

with open('apartment1.json', encoding='utf-8') as f:
    json_data = json.loads(f.read())
    print(json_data['Apartment'])
    ''''new_data = filter_list(3, 2, 12000, json_data)
    print(new_data)'''