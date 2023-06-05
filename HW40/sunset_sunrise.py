from datetime import datetime

from request import Request


class SunSetRise:

    def __init__(self, city):
        self.request = Request(city)

    def get_todays_sun_set_rise(self):
        data = self.request.get_current_sun_data_from_api().json()

        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.fromtimestamp(data["sys"]["sunset"])

        print("today's sunset = ", sunrise)
        print("today's sunrise = ", sunset)
