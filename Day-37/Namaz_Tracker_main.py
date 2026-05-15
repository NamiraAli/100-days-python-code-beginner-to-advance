import requests
from datetime import datetime

USERNAME="username"
TOKEN="token"
GRAPH_ID="graphid"
# TODAY=datetime(year=2026,month=5,day=15)
TODAY=datetime.now()
##create user

pixela_endpoint="https://pixe.la/v1/users"

parameter={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(url=pixela_endpoint,json=parameter)
# print(response.text)

##step 2: create a graph

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameter={
    "id":GRAPH_ID,
    "name":"Namaz Tracker",
    "unit":"times",
    "type":"int",
    "color":"momiji"

}

header={
    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=graph_endpoint,json=graph_parameter,headers=header)
# print(response.text)

##post a pixel

pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today=datetime.now()



pixel_parameter={
    "date":TODAY.strftime("%Y%m%d"),
    "quantity":input("HOW MANY PRAYERS DID YOU PRAY TODAY :: ")
}
#
response = requests.post(url=pixel_endpoint,json=pixel_parameter,headers=header)
print(response.text)

##to update the pixel

put_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY.strftime('%Y%m%d')}"
put_parameter={
    "quantity":"3"
}
#
# response=requests.put(url=put_endpoint,json=put_parameter,headers=header)
# print(response1.text)

##delete a pixel

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY.strftime('%Y%m%d')}"
# response=requests.delete(url=delete_endpoint,headers=header)
# print(response.text)
