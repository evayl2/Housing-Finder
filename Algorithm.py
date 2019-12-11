from geopy.geocoders import Nominatim

geolocator = Nominatim()
def get_loca(address):
    return geolocator.geocode(address)

def get_key(elem):
    return dist[elem]

def get_dist(a,b):
    loca1=get_loca(d[a].address)
    loca2=get_loca(d[b].address)
    return abs(loca1.latitude-loca2.latitude)+abs(loca1.longitude-loca2.longitude)

def rank_dist(apts,blgs):
    dist=[0 for _ in apts]
    for i in range(len(apts)):
        for blg in blgs:
            dist[i]+=get_dist(apt[i],blg)

    sort(key=get_key)