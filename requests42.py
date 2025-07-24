import requests
response = requests.get("https://api.football-data.org/v4/teams/5/matches")
print(response.json())

