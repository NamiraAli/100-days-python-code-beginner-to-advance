import requests


parameter={
    "amount":10,
    "type":'boolean',
    "category":18
}
response=requests.get("https://opentdb.com/api.php",params=parameter) #using API from TRIVIA Database
response.raise_for_status()
data=response.json()
question_data=data["results"]


# import requests
# parameter if needed request.get() raise_for_status() response.json() use data
#
