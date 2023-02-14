import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
response.raise_for_status() 

data = response.json()["iss_position"]
longitude = data["longitude"]
latitude = data["latitude"]

iss_position = (longitude, latitude)
print(iss_position)