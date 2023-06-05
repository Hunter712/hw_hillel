from hw40.get_temperature import Temperature
from hw40.get_wind_speed import WindSpeed
from hw40.sun_set_rise import SunSetRise


class System:

    def __init__(self, city, country_code):
        self.temperature = Temperature(city, country_code)
        self.wind = WindSpeed(city)
        self.sun = SunSetRise(city)

    def current_weather_conditions(self):
        self.temperature.get_current_temperature()
        self.wind.get_current_wind_speed()
        self.sun.get_todays_sun_set_rise()

    def weather_forecast(self):
        self.temperature.get_temperature_forecast()


if __name__ == "__main__":
    system = System("Kharkiv", "UA")
    system.current_weather_conditions()
