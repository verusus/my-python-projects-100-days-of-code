# with open("weather_data.csv", mode="r") as csv_file:
#     data = csv_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp_value = int(row[1])
#             temperatures.append(temp_value)
#     print(temperatures)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["temp"].max())
# print(data.temp)
# print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# print("fahrenheit degree= ", int(monday.temp)*9/5+32)
new_data = data["Primary Fur Color"].value_counts()
# print(new_data)
new_dict = {
    "Fur Color": ["Gay", "Cinnamon", "Black"],
    "Count": [new_data["Gray"], new_data["Cinnamon"], new_data["Black"]]
}
new_data_frame = pandas.DataFrame(new_dict)
print(new_data_frame)
# print(new_data_frame)
new_data_frame.to_csv("squirrel_count.csv")

