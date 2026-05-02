import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
#print(response) #response code, not plain data

response.raise_for_status()

data = response.json() # {'iss_position': {'latitude': '-50.5508', 'longitude': '103.5198'}, 'message': 'success', 'timestamp': 1774473534}
position = response.json()["iss_position"]
print(position)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)