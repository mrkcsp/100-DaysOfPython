import requests
from datetime import datetime

MY_LAT = "40.719900"
MY_LONG = "8.565414"

api = "https://api.sunrise-sunset.org/json"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url=api, params=parameters)
response.raise_for_status()

data = response.json()["results"]

sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()
hour = time_now.hour

print(sunrise, sunset, hour)


    