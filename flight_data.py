from flight_search import FlightSearch
import os
class FlightData:
    FLIGHT_ID = os.environ["FLIGHT_ID"]
    FLIGHT_API_KEY = os.environ["FLIGHT_API_KEY"]
    FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
