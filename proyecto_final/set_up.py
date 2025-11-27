import json

def get_location():
    pass

def set_location(city, country, latitude, longitude):
    location_data = {
        "location": {
            "city": city,
            "country": country,
            "latitude": latitude,
            "longitude": longitude
        }
    }
    with open("preferences.json", "w") as file:
        json.dump(location_data, file)
