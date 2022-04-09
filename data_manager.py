import requests
class DataManager:
    SHEETY_ENDPOINT = "https://api.sheety.co/3672d30b0c3d48f9003f58ea383f25ed/flightDeals/prices"
    sheety_response = requests.get(url=SHEETY_ENDPOINT)
    sheety_response.raise_for_status()

    sheety_data = sheety_response.json()
    country_code_list = [x['iataCode'] for x in sheety_data["prices"]]
    country_price_dic = {x['iataCode']: x['lowestPrice'] for x in sheety_data["prices"]}


