import requests
from datetime import datetime
import smtplib
import time


MY_LAT = "40.719900"
MY_LONG = "8.565414"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

EMAIL = "test@email.com"
PASSWORD = "pass"

def is_nigth():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()["results"]

    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else: 
        return False
    
def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    #print(response) #response code, not plain data

    response.raise_for_status()

    data = response.json() # {'iss_position': {'latitude': '-50.5508', 'longitude': '103.5198'}, 'message': 'success', 'timestamp': 1774473534}
    position = response.json()["iss_position"]
    print(position)

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    iss_position = (longitude, latitude)

    #print(iss_position)

    lat_range = range(MY_LAT-5, MY_LAT+5) # 35.719900 - 45.719900
    lng_range = range(MY_LONG-5, MY_LONG+5)

    if iss_position[0] in lat_range and iss_position[1] in lng_range:
        print("ISS is close")
        return True
    else:
        return False

#If the ISS is close to my current position and is currently dark send me an email
#BONUS, run the code every 60 seconds


while True: #if ISS is over you this while spams a mail every minute, pay attention
    time.sleep(60)
    if is_iss_overhead and is_nigth:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs="testmail@mail.com", msg="Subject:Look UP!\n\nThe ISS is above you!")


       