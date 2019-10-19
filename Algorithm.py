from geopy.geocoders import Nominatim

geolocator = Nominatim()
def get_loca(address):
    return geolocator.geocode(address)