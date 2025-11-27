from typing import Optional, List


class Result:
    id: Optional[int]
    name: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    elevation: Optional[int]
    feature_code: Optional[str]
    country_code: Optional[str]
    admin1_id: Optional[int]
    admin2_id: Optional[int]
    admin3_id: Optional[int]
    timezone: Optional[str]
    population: Optional[int]
    postcodes: Optional[List[int]]
    country_id: Optional[int]
    country: Optional[str]
    admin1: Optional[str]
    admin2: Optional[str]
    admin3: Optional[str]

    def __init__(self, id: Optional[int], name: Optional[str], latitude: Optional[float], longitude: Optional[float], elevation: Optional[int], feature_code: Optional[str], country_code: Optional[str], admin1_id: Optional[int], admin2_id: Optional[int], admin3_id: Optional[int], timezone: Optional[str], population: Optional[int], postcodes: Optional[List[int]], country_id: Optional[int], country: Optional[str], admin1: Optional[str], admin2: Optional[str], admin3: Optional[str]) -> None:
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation
        self.feature_code = feature_code
        self.country_code = country_code
        self.admin1_id = admin1_id
        self.admin2_id = admin2_id
        self.admin3_id = admin3_id
        self.timezone = timezone
        self.population = population
        self.postcodes = postcodes
        self.country_id = country_id
        self.country = country
        self.admin1 = admin1
        self.admin2 = admin2
        self.admin3 = admin3


class ForecastDaily:
    results: Optional[List[Result]]
    generationtime_ms: Optional[float]

    def __init__(self, results: Optional[List[Result]], generationtime_ms: Optional[float]) -> None:
        self.results = results
        self.generationtime_ms = generationtime_ms
