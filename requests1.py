import requests
response=requests.get("https://www.geeksforgeeks.org/")
print(response)
print(response.status_code)
response2=requests.get("https://www.cricbuzz.com/cricket-match/live-scores")
print(response2.status_code)
print(response2.content)
