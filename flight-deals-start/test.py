#
#
#
# class FlightData:
#     # This class is responsible for structuring the flight data.
#     def __init__(self, price, origin_city, stop_overs=0):
#         self.price = price
#         self.origin_city = origin_city
#
#         self.stop_overs = stop_overs
#         # self.stop_overs = kwargs.get("stop_overs")
#     # def __init__(self, price, origin_city, **kwargs):
#     #     self.price = price
#     #     self.origin_city = origin_city
#     #
#     #     self.stop_overs = 0
#     #     # self.stop_overs = kwargs.get("stop_overs")
# flight_data = FlightData(30, "tetouan", stop_overs=1)
# # flight_data.stop_overs = 1   # to modify the value of kwargs
# print(flight_data.price, "_", flight_data.stop_overs)
from data_manager import DataManager

# data_manager = DataManager()
# users_data = data_manager.get_sheet_data("users")
# print(users_data)
from notification_manager import NotificationManager
user_data = [{'firstName': 'hamid', 'lastName': 'salhi', 'email': 'essalhi12345@gmail.com', 'id': 2},
             {'firstName': 'hamid', 'lastName': 'yahoo', 'email': 'essalhi12345@yahoo.com', 'id': 3}]
notification_manager = NotificationManager()
notification_manager.send_emails(message="this a test", users_data=user_data)

