import requests as rq
import json
url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.21&current_weather=true"
r=rq.get(url)
print(r)
data=r.json()
print(json.dumps(data, indent=4))
