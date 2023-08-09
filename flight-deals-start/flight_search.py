from pprint import pprint
import requests
from datetime import datetime, timedelta
from flight_data import FlightData


TEGUILA_ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = "rG0bo0JwJNe-SU2TAEH2cOLXrd0OQsTD"

DEPARTURE_AIRPORT_CODE = "CMN"
DATE_FROM = (datetime.today() + timedelta(days=1)).strftime("%d/%m/%Y")
DATE_TO = (datetime.today() + timedelta(days=30*6)).strftime("%d/%m/%Y")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_iata_code(self, city_name):
        search_params = {
            "term": city_name,
            "location_types": "city",
            "limit": 1,
        }
        header = {
            "apikey": API_KEY,
        }
        response = requests.get(url=f"{TEGUILA_ENDPOINT}/locations/query", headers=header, params=search_params)
        response.raise_for_status()
        code = response.json()['locations'][0]['code']
        return code

    def search_flight_to(self, destination_city_code):
        header = {
            "apikey": API_KEY,
        }

        query = {
            "fly_from": DEPARTURE_AIRPORT_CODE,
            "fly_to": destination_city_code,
            "date_from": DATE_FROM,
            "date_to": DATE_TO,
            "flight_type": "round",   # Available values for flight_type : round, oneway
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(url=f"{TEGUILA_ENDPOINT}/v2/search", headers=header, params=query)
        response.raise_for_status()
        try:
            data = response.json()['data'][0]
            # pprint(data)

        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=f"{TEGUILA_ENDPOINT}/v2/search", headers=header, params=query)
            response.raise_for_status()
            try:
                data = response.json()['data'][0]
            except IndexError:
                print("there is no flights to ", destination_city_code)
            else:
                # pprint(data)
                flight_data = FlightData(
                    price=data["price"],
                    booking_link=data['deep_link'],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                booking_link=data['deep_link'],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
