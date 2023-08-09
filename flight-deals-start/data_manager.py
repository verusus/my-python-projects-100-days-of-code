import requests
from pprint import pprint

# This class is responsible for talking to the Google Sheet.
SHEETY_ENDPOINT = "https://api.sheety.co/d7877bfc726190cb564b1ef043265e97/copieDeFlightDeals/"
SHEETY_POST_ENDPOINT = "https://api.sheety.co/d7877bfc726190cb564b1ef043265e97/copieDeFlightDeals/prices"


class DataManager:

    def get_sheet_data(self, sheet):
        response = requests.get(url=SHEETY_ENDPOINT+f"{sheet}")
        response.raise_for_status()
        return response.json()[sheet]

    def update_iata(self, record_id, record_update):
        reponse = requests.put(url=SHEETY_POST_ENDPOINT+"/"+str(record_id), json=record_update)
        reponse.raise_for_status()
