import requests as rq
url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.21&current_weather=true"
r=rq.get(url)
print(r.url)
print(r.status_code)
print(r.request)
