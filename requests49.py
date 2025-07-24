import requests
import time  # You forgot to import this

while(True):
url = "https://api.cricapi.com/v1/currentMatches?apikey=c67ed518-9f52-4320-ba9f-561e18d7ce6b&offset=0"
r = requests.get(url)
print(r.status_code)

data = r.json()
matches = data["data"]

for match in matches:
    teams = match.get("teams", [])
    if "India" in teams:
        # This is your match
        match_name = match.get("name", "Unknown Match")
        match_type = match.get("matchType", "")
        status = match.get("status", "")
        score_list = match.get("score", [])

        print(f"\n{match_name} ({match_type})")
        print(f"Status: {status}")

        if score_list:
                score = match.get("score", [])[0]  # re-fetch score each time (optional, but safer)
                runs = score.get("r")
                wickets = score.get("w")
                overs = score.get("o")
                inning = score.get("inning")

                print(f"{inning}: {runs}/{wickets} in {overs} overs")

        break  # stop after finding first India match
    time
