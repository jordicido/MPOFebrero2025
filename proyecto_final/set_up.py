import json

def get_location():
    with open("preferences.json", "r") as file:
        result = json.load(file)
        if "location" in result:
            return result["location"]
        
        return None

def set_location(city, country, latitude, longitude):
    location_data = {
        "location": {
            "name": city,
            "country": country,
            "latitude": latitude,
            "longitude": longitude
        }
    }
    with open("preferences.json", "w") as file:
        json.dump(location_data, file)
