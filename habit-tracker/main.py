import requests
from datetime import datetime

TOKEN = "hellopixela1923092347450384slerewfsk"
USERNAME = "hamid1"
GRAPH_ID = "graph1"
GRAPH_NAME = "Cycling Graph"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POST_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

today = datetime.today()
UPDATE_OR_DELETE_ENDPOINT = f"{POST_ENDPOINT}/{today.strftime('%Y%m%d')}"


user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_param)
# print(response.text)


graph_config = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

post_put_delete_header = {
    "X-USER-TOKEN": TOKEN,
}
# # creating the tracker graph
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=post_put_delete_header)
# print(response.text)


# posting a pixel
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many Kilometers did you cycle today? "),
}

response = requests.post(url=POST_ENDPOINT, json=post_config, headers=post_put_delete_header)
print(response.text)

# updating today's data using put http request
put_config = {
    "quantity": "8",
}

# response = requests.put(url=UPDATE_ENDPOINT, json=put_config, headers=post_put_header)
# print(response.text)

# Deleting today's pixel from the graph
# response = requests.delete(url=UPDATE_OR_DELETE_ENDPOINT, json=post_put_delete_header, headers=post_put_delete_header)
# print(response.text)

