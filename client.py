
import requests

url = "http://weather.jacksalici.com/data/report"

data = {
   "dateutc":"2023-05-07 26:39:35",
   "tempinf":"72.68",
   "humidity":"48",
   "winddir":"310",
   "windspeedmph":"0.22",
   "windgustmph":"1.12",
   "maxdailygust":"4.47",
   "solarradiation":"661.25",
   "uv":"6",
   "rainratein":"0.000",
}



resp = requests.post(url, json=data)

print(resp.content)
