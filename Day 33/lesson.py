import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notifv.org/iss-now.json")
# response.raise_for_status()
# # print(response)
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

MY_LAT = 180
MY_LONG = 0
current_hour = datetime.now().hour
print(f"The current hour is: {current_hour}")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

sunrise_hour = data["result"]["sunrise"].split("T")[1].split(":")[0]
sunset_hour = data["result"]["sunset"].split("T")[1].split(":")[0]

# print(sunrise, sunset)
print(sunrise_hour)
print(sunset_hour)
print()
