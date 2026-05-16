import requests
from datetime import datetime

APP_ID="App_id from app.100daysofpython/exercise "
APP_KEY="App_key_from app.100daysofpython/exercise"

GENDER = "female"
WEIGHT_KG = 78
HEIGHT_CM = 178
AGE = 22


ENDPOINT="https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

header={
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

parameter_req={
    "query":input("enter what you did : "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

post_response=requests.post(url=ENDPOINT,headers=header,json=parameter_req)
result = post_response.json()
# exercise=result["exercises"]["name"]
# duration=result["exercises"]["duration_min"]
# calories=result["exercises"]["nf_calories"]
#
# print(exercise,duration,calories)
print(result)


##sheety
sheety_get_url="sheety get url"
sheety_post_url="sheety post url"

authentication={
    "Authorization": "authentication code"
}


today_date=datetime.now().strftime("%d-%m-%Y")
today_time=datetime.now().strftime("%I:%M %p")
print(today_date,today_time)

for exercise in result["exercises"]:
    workout_input={
        "workout":{
            "Date":today_date,
            "Time":today_time,
            "Exercise":exercise['name'].title(),
            "Duration":exercise['duration_min'],
            "Calories":exercise['nf_calories']
    }
    }
##post result in sheet

post_result_in_sheet=requests.post(url=sheety_post_url,json=workout_input,headers=authentication)
post_result_in_sheet.raise_for_status()
print(post_result_in_sheet.text)
