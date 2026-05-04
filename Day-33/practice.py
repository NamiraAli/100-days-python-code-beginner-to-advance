import requests
import datetime as dt
MY_LAT=19.970461
MY_LNG=79.301483
parameters={
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0

}

response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"]
sunset=data["results"]["sunset"]
time_now=dt.datetime.now()

# print("sunrise : ",sunrise)
#spliting the string
print(sunrise.split("T")[1].split(":")[0]) #this separates the data based on the notation we want in list herer whereever T will appear it will break the data
print(sunset.split("T")[1].split(":")[0])

sunrise=int(sunrise.split("T")[1].split(":")[0]) #this separates the data based on the notation we want in list herer whereever T will appear it will break the data

print("time_now :",time_now.hour)
