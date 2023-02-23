# Author: Matt Williams
# Version: 2/13/2023
# Pricing:
# - Geocoding API -> 0.005 USD per request
# - Places API/Nearby Search -> starts at 0.04 USD per request
# - Distance Matrix API -> starts at 0.005 USD per request

# API call Sequence
# - Send address to Geocoding API to get the longitude and latitude.
# - Send longitude, latitude, radius, and place type to Nearby Search to get places nearby.
# -- will need to do searches for each Place type of interest.
# - For each place nearby calculate the distance with Distance Matrix.


from decouple import config
from googlemaps import Client, geocoding, places, distance_matrix
import json
import os

API_KEY = config("API_KEY")
HOME_ADDRESS = config("HOME_ADDRESS")
CWD = os.getcwd()
TEST_GEOCODE_PATH = os.path.join(CWD,"test_geocode_file.json")
TEST_NEARBY_PATH = os.path.join(CWD, "test_nearby_file.json")
TEST_DISTANCE_PATH = os.path.join(CWD, "test_distance_file.json")
TEST_RADIUS = 8050 # meters


POTENTIAL_PLACE_TYPES= [
    "supermarket", 
    "pharmacy",
    "hospital",
    "drugstore",
    "doctor",
    "cafe",
    "convenience_store",
    "department_store",
    "restaurant",
    "store",
    "shopping_mall",
    "bakery"
]

def read_test_data(file_path):
    with open(file_path, mode = "r+", encoding="utf-8") as file: 
        return json.load(file)

def save_test_data(file_path, data):
    with open(file_path, mode = "w+", encoding="utf-8") as file:
        json.dump(data, file, indent = 1)



def grab_geocode_data():
    gmaps = Client(key=API_KEY)
    r = geocoding.geocode(gmaps, HOME_ADDRESS)
    save_test_data(TEST_GEOCODE_PATH, r)



def grab_nearby_data(lat, lng):
    gmaps = Client(key=API_KEY)
    r = places.places_nearby(client = gmaps,
                             location = (lat,lng),
                             radius=TEST_RADIUS,
                             type="pharmacy")

    save_test_data(TEST_NEARBY_PATH, r)

def grab_distance_data(org, dest):
    gmaps = Client(key=API_KEY)
    r = distance_matrix.distance_matrix(gmaps, org, dest)
    save_test_data(TEST_DISTANCE_PATH, r)

if __name__ == "__main__":
    #grab_geocode_data()
    
    #geo_data = read_test_data(TEST_GEOCODE_PATH)
    #lat = geo_data[0]['geometry']['location']['lat']
    #lng = geo_data[0]['geometry']['location']['lng']
    #grab_nearby_data(lat, lng)

    geo_data = read_test_data(TEST_GEOCODE_PATH)
    nearby_data = read_test_data(TEST_NEARBY_PATH)

    home_place_id = f"place_id:{geo_data[0]['place_id']}"
    dest_place_id = f"place_id:{nearby_data['results'][0]['place_id']}"

    grab_distance_data(home_place_id, dest_place_id)




    
    