import requests

api_key = "708372294dd1f65f7d6c184bab415939"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = 'Dharwad'
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x["main"]
    temp_cel = round(y["temp"] - 273, 1)
    temp_fah = round((temp_cel * 1.8) + 32, 1)
