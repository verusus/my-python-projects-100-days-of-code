from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from notification_manager import NotificationManager


# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()


sheet_data = data_manager.get_sheet_data("prices")
# pprint(sheet_data)

for record in sheet_data:
    # record to be updated
    record_update = {
        "price": {
            "iataCode": flight_search.get_iata_code(record['city']),
        }
    }
    data_manager.update_iata(record['id'], record_update)

# re-get updated data
sheet_data = data_manager.get_sheet_data(sheet="prices")
# sheet_data = [{
#     "city": "Cape Town",
#     "iataCode": "CPT",
#     "lowestPrice": 10000,
# }
# ]
for record in sheet_data:
    flight_data = flight_search.search_flight_to(record['iataCode'])

    if flight_data is None:
        continue      # skip this iteration

    message = f"Low price alert! Only £{flight_data.price} to fly from " \
              f"{flight_data.origin_city}-{flight_data.origin_airport} to " \
              f"{flight_data.destination_city}-{flight_data.destination_airport}, " \
              f"from {flight_data.out_date} to {flight_data.return_date}.\n"
    if flight_data.stop_overs > 0:
        message += f"Flight has {flight_data.stop_overs} stop over, via {flight_data.via_city}.\n"
    message += flight_data.booking_link
    if flight_data.price <= record['lowestPrice']:
        users_data = data_manager.get_sheet_data("users")
        # notification_manager.send_sms(message)
        notification_manager.send_emails(message, users_data)
        print(message)
        print("emails sent!")






