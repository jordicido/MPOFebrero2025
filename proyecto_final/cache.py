import json
from datetime import datetime

CACHE_EXPIRATION_TIME = 1800

def get_cache_data():
    with open("cache.json", "r") as file:
        data = json.load(file)
        if "timestamp" in data:
            delta_time = datetime.now() - datetime.fromisoformat(data["timestamp"])
            if delta_time.total_seconds() <= CACHE_EXPIRATION_TIME:
                return data["forecast"]
            
    return None

def set_data_to_cache(forecast_data):
    data = {"timestamp": datetime.now().isoformat(), "forecast": forecast_data}
    with open("cache.json", "w") as file:
        json.dump(data, file)