import configparser
import requests


class Request:
    KEY = "X-RapidAPI-Key"
    HOST = "X-RapidAPI-Host"

    def __init__(self, city):
        self.city = city
        self.config = configparser.ConfigParser()
        self.config.read("settings.ini")

    def get_current_sun_data_from_api(self):
        return requests.get(self.config["sun"]["url_for_searching_current_sun_info"] + self.city,
                            headers={Request.KEY: self.config["sun"][Request.KEY],
                                     Request.HOST: self.config["sun"][Request.HOST]})

    def get_location_id_from_api(self):
        return requests.get(self.config["temperature"]["url_for_searching_location"] + self.city,
                            headers={Request.KEY: self.config["temperature"][Request.KEY],
                                     Request.HOST: self.config["temperature"][Request.HOST]})

    def get_current_temperature_from_api(self, id):
        return requests.get(self.config["temperature"]["url_for_searching_current_temp"] + str(id),
                            headers={Request.KEY: self.config["temperature"][Request.KEY],
                                     Request.HOST: self.config["temperature"][Request.HOST]})

    def get_forecast_temperature_from_api(self, id):
        return requests.get(self.config["temperature"]["url_for_searching_forecast_temp"] + str(id),
                            headers={Request.KEY: self.config["temperature"][Request.KEY],
                                     Request.HOST: self.config["temperature"][Request.HOST]})

    def get_wind_speed_from_api(self):
        return requests.get(self.config["wind"]["url_for_searching_current_wind_speed"],
                            headers={Request.KEY: self.config["wind"][Request.KEY],
                                     Request.HOST: self.config["wind"][Request.HOST]}, params={"city": self.city})
