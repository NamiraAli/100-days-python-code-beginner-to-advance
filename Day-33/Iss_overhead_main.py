import requests #to work with api
import datetime as dt
import smtplib #to send mail
import time

MY_EMAIL="testmail@gmail.com"
MY_PASS="Pass@123"
MY_LAT=11.970461
MY_LNG=70.301483

def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")  #API OF ISS
    # print(response) #output of response is <Response [200]>   #200 is response code or status_code
    #something like 1xx hold on ,2xx here you go ,3xx go away, 4xx you screwed up, 5xx i screwed up

    response.raise_for_status() #to get hold of every error

    data=response.json() #to get the data json
    iss_longitude=float(data["iss_position"]["longitude"])
    iss_latitude=float(data["iss_position"]["latitude"])

    #your position is within iss +5 or _5 degrees of iss position

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LAT-5 <= iss_longitude <= MY_LNG+5:
        print(f"{iss_latitude},{iss_longitude} is visible")
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0

    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters) #API OF SUNRISE SUNSET
    response.raise_for_status()
    data = response.json()
    sunrise =data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise = int(sunrise.split("T")[1].split(":")[0])
    sunset = int(sunset.split("T")[1].split(":")[0])

    time_now=dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        # print("its dark")
        # print("sunrise:",sunrise)
        # print("sunset:",sunset)
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="Subject:LoOk up \n\n The iss is above you")
