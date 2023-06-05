from temperature import Temperature
from wind_speed import WindSpeed
from sunset_sunrise import SunSetRise


class System:

    def __init__(self, city):
        self.temperature = Temperature(city)
        self.wind = WindSpeed(city)
        self.sun = SunSetRise(city)

    def current_weather_conditions(self):
        try:
            self.temperature.get_current_temperature()
        except Exception as message:
            print("Something happened with temperature server")

        try:
            self.wind.get_current_wind_speed()
        except Exception:
            print("Something happened with wind server")

        try:
            self.sun.get_todays_sun_set_rise()
        except Exception:
            print("Something happened with sun server")

    def weather_forecast(self):
        try:
            self.temperature.get_temperature_forecast()
        except Exception:
            print("Something happened with temperature server")


if __name__ == "__main__":
    system = System("Kharkiv")
    system.current_weather_conditions()
