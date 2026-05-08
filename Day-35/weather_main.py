import requests
from twilio.rest import Client


MY_ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
api_key="123piu"
account_sid="xyz"
auth_token="abc"

weather_parameter={
    "lat":19.970461,
    "lon":79.301483,
    "cnt":4,
    "appid":api_key
}
# response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")
# response=requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=19.970461&lon=79.301483&cnt=4&appid=279960952700add0124f9c6dd110f001")

response=requests.get(MY_ENDPOINT,params=weather_parameter)
print(f"{response.status_code} : code check")
data=response.json()

#twilio for sms api

will_rain=False
for x in range(0,4):
    weather=data["list"][x]["weather"][0]["id"]
    if weather > 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="not sunny",
        from_="123456789",
        to="987654321"
    )
    print(message.status)
