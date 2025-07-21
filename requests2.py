import requests

url = "https://v3.football.api-sports.io/teams?name=bayern"
headers = {
    "x-apisports-key": "YOUR_API_KEY_HERE"
}
res = requests.get(url, headers=headers)
print(res.json())

