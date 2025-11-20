from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Daily:
    time: Optional[List[datetime]]
    weather_code: Optional[List[int]]
    temperature_2m_max: Optional[List[float]]
    temperature_2m_min: Optional[List[float]]
    sunrise: Optional[List[str]]
    sunset: Optional[List[str]]
    precipitation_probability_max: Optional[List[int]]


@dataclass
class DailyUnits:
    time: Optional[str]
    weather_code: Optional[str]
    temperature_2m_max: Optional[str]
    temperature_2m_min: Optional[str]
    sunrise: Optional[str]
    sunset: Optional[str]
    precipitation_probability_max: Optional[str]


@dataclass
class ForecastDaily:
    latitude: Optional[float]
    longitude: Optional[float]
    generationtime_ms: Optional[float]
    utc_offset_seconds: Optional[int]
    timezone: Optional[str]
    timezone_abbreviation: Optional[str]
    elevation: Optional[int]
    daily_units: Optional[DailyUnits]
    daily: Optional[Daily]

    def __init__(self, latitude: Optional[float], longitude: Optional[float], generationtime_ms: Optional[float], utc_offset_seconds: Optional[int], timezone: Optional[str], timezone_abbreviation: Optional[str], elevation: Optional[int], daily_units: Optional[DailyUnits], daily: Optional[Daily]) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.generationtime_ms = generationtime_ms
        self.utc_offset_seconds = utc_offset_seconds
        self.timezone = timezone
        self.timezone_abbreviation = timezone_abbreviation
        self.elevation = elevation
        self.daily_units=DailyUnits(**daily_units)
        self.daily=Daily(**daily)
