import requests
from datetime import datetime
import os


GENDER = "male"
WEIGHT_KG = "84"
HEIGHT_CM = "83"
AGE = "22"

# APP_ID = "6165db6d"
APP_ID = os.environ.get('APP_ID')
# API_KEY = "09fd53fd4a1c65a0c2a901967ec303cf"
API_KEY = os.environ.get('API_KEY')

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# sheety_endpoint = "https://api.sheety.co/75fd120e34541fbb0b65e7d4633cc667/myWorkouts/workouts"
sheety_endpoint = os.environ.get('sheety_endpoint')

# TOKEN = os.environ.get('TOKEN')

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
print(exercise_response.json())

results = exercise_response.json()
print(results)
exercises = results["exercises"]


for item in exercises:
    exercise = item["name"].title()
    duration = item["duration_min"]
    calories = item["nf_calories"]

    # length of the list is equal to number of rows I will add

    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")
    workouts = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    # basic auth   # for learning purposes I will let username & password code here even I set them in the eviron var
    # sheety_response = requests.post(url=sheety_endpoint, json=workouts, auth=('hamid', 'as12958@##al32SADsldp*)9'))

    # Bearer Token Authentication : it means that header bears the token auth key
    # sheety_header = {
    #     "Authorization": "Basic aGFtaWQ6YXMxMjk1OEAjI2FsMzJTQURzbGRwKik5",
    # }
    sheety_header = {
        "Authorization": os.environ['TOKEN'],
    }
    sheety_response = requests.post(url=sheety_endpoint, json=workouts, headers=sheety_header)
    sheety_response.raise_for_status()
    print(sheety_response.text)

