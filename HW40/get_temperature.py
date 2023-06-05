import requests
import json


class Temperature:
    HEADERS = {
        "X-RapidAPI-Key": "ccb88f910fmshfb301a28740ba83p177a4ejsncf387e878ed8",
        "X-RapidAPI-Host": "foreca-weather.p.rapidapi.com"
    }

    def __init__(self, city, country_code):
        self.city = city
        self.country_code = country_code

    def get_current_location_id(self):
        url = f"https://foreca-weather.p.rapidapi.com/location/search/{self.city}"
        response = requests.get(url, headers=Temperature.HEADERS,
                                params={"lang": "en", "country": self.country_code})
        data = json.loads(response.text)
        return data["locations"][0]["id"]

    def get_current_temperature(self):
        url = f"https://foreca-weather.p.rapidapi.com/current/{self.get_current_location_id()}"
        response = requests.get(url, headers=Temperature.HEADERS)
        data = json.loads(response.text)
        print("current temperature = ", data["current"]["temperature"])

    def get_temperature_forecast(self):
        url = f"https://foreca-weather.p.rapidapi.com/forecast/daily/{self.get_current_location_id()}"

        response = requests.get(url, headers=Temperature.HEADERS)
        data = json.loads(response.text)
        for i in range(len(data["forecast"])):
            print(data["forecast"][i]["date"], "Min temp = ", data["forecast"][i]["minTemp"],
                  "Max temp = ", data["forecast"][i]["maxTemp"])


