import requests as rq
url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.21&current_weather=true"
r=rq.get(url)
api_data=r.json()
for key in api_data:
    print(key,":",api_data[key])
