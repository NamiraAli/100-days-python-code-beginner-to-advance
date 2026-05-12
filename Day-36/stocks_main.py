import requests
from twilio.rest import Client

account_sid="accound_sid id from twilio "
auth_token="auth_token id from twilio "

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key ="my api key from stock endpoint"
news_api_key="my api key from news endpoint"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameter={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":api_key,
}

parameter_news={
    "q":COMPANY_NAME,
    "apikey":news_api_key,
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

response = requests.get(STOCK_ENDPOINT, params=parameter)
data = response.json()
i_want=data["Time Series (Daily)"]  #this is a dict
data_list=[value for (key ,value) in i_want.items()]  #we made it a list with only values

# yesterday_data_close=data_list[0]["4. close"]  #getting close data
# print(yesterday_data_close)

response1=requests.get(NEWS_ENDPOINT, params=parameter_news)
data_news=response1.json()
i_want_news1=data_news["articles"][0]["title"]
i_want_news2=data_news["articles"][1]["title"]
i_want_news3=data_news["articles"][2]["title"]

## yesterday and day before yesterday closing data

yesterday_data_close=data_list[0]["4. close"]  #getting close data
print(yesterday_data_close)

day_before_yesterday_data_close=data_list[1]["4. close"]
print(day_before_yesterday_data_close)


## percentage calculation

difference=abs(float(yesterday_data_close)-float(day_before_yesterday_data_close))
print(f"{difference:.4f}")

percentage=difference/float(day_before_yesterday_data_close)*100
print(f"{percentage:.4f}%")


##get news title  top 3 ::

if percentage>3:
    print(f"NEWS\n1.{i_want_news1} \n2.{i_want_news2} \n3.{i_want_news3}")




## get news description wrt tesla

print("\nNEWS DESCRIPTION ")
get_news_article=data_news["articles"]

y=0
for x in range(len(get_news_article)):
    while y<3:
        if "Tesla" in get_news_article[x]["title"]:
            if get_news_article[x]["description"] is not None:
                print(get_news_article[x]["description"])
                y = y + 1
        break

#get data in list headline and description

news_data_top=["headline : "+ get_news_article[x]["title"]+ "\nBrief : " +get_news_article[x]["description"] for x in range(0,4)]
print(news_data_top)

#twilio usage

client=Client(account_sid,auth_token)
for x in range (0,3):
    message=client.messages.create(
        body=news_data_top[x],
        from_="my_twilio_number",
        to="my number"
    )
    print(message.status)


