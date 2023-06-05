
from request import Request


class WindSpeed:

    def __init__(self, city):
        self.request = Request(city)

    def get_current_wind_speed(self):

        data = self.request.get_wind_speed_from_api().json()
        print("current wind speed = ", data["wind_speed"])

