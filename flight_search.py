import requests
from data_manager import DataManager
from notification_manager import NotificationManager
import os
class FlightSearch:
    def __init__(self):
        self.price_dic = DataManager().country_price_dic
        self.country_list = DataManager().country_code_list
        self.FLIGHT_ID = os.environ["FLIGHT_ID"]
        self.FLIGHT_API_KEY = os.environ["FLIGHT_API_KEY"]
        self.FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
        self.flight_header = {
            "apikey": self.FLIGHT_API_KEY
        }


    def cheap_flight(self):
        for country in self.country_list:
            flight_params = {
                "fly_from": "LGA",
                "fly_to": country,
                "dateFrom": "15/04/2022",
                "dateTo": "06/10/2022",
                "curr": "USD"
            }

            flight_response = requests.get(url=self.FLIGHT_ENDPOINT, params=flight_params, headers=self.flight_header)
            flight_response.raise_for_status()
            data = flight_response.json()
            ticket_price = data['data'][4]['price']  # Works!
            if self.price_dic[country] >= ticket_price:
                message = NotificationManager()
                message.send_message(destination=country, price=self.price_dic[country],
                                     location=flight_params["fly_from"])

