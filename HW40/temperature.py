from request import Request


class Temperature:

    def __init__(self, city):
        self.city = city
        self.request = Request(city)

    def get_current_location_id(self):

        data = self.request.get_location_id_from_api().json()
        return data["locations"][0]["id"]

    def get_current_temperature(self):
        data = self.request.get_current_temperature_from_api(self.get_current_location_id()).json()
        print("current temperature = ", data["current"]["temperature"])

    def get_temperature_forecast(self):
        data = self.request.get_forecast_temperature_from_api(self.get_current_location_id()).json()
        for i in range(len(data["forecast"])):
            print(data["forecast"][i]["date"], "Min temp = ", data["forecast"][i]["minTemp"],
                  "Max temp = ", data["forecast"][i]["maxTemp"])


