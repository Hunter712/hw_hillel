import requests
import json


class SunSetRise:
    HEADERS = {
        "X-RapidAPI-Key": "50474e707fmshbf6a2ebfa90e980p1098aejsn55ec09aee92c",
        "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
    }

    def __init__(self, city):
        self.city = city

    def get_todays_sun_set_rise(self):
        url = f"https://open-weather13.p.rapidapi.com/city/{self.city}"

        response = requests.get(url, headers=SunSetRise.HEADERS)
        data = json.loads(response.text)
        print("today's sunset = ", data["sys"]["sunrise"])
        print("today's sunrise = ", data["sys"]["sunset"])

