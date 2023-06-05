import requests
import json


class WindSpeed:
    HEADERS = {
        "X-RapidAPI-Key": "ccb88f910fmshfb301a28740ba83p177a4ejsncf387e878ed8",
        "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
    }
    URL = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

    def __init__(self, city):
        self.city = city

    def get_current_wind_speed(self):

        response = requests.get(WindSpeed.URL, headers=WindSpeed.HEADERS, params={"city": self.city})
        data = json.loads(response.text)
        print("current wind speed = ", data["wind_speed"])

    def get_wind_speed_forecast(self):
        pass
