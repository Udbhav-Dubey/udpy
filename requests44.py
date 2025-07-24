import requests
r=requests.get(url)
print(r.status_code)
data=r.json()
matches=data["data"]
for match in matches:
    teams = match.get("teams", [])
if "India" in teams:
    # This is your match
         match_name = match.get("name", "Unknown Match")
         match_type = match.get("matchType", "")
         status = match.get("status", "")
         score_list = match.get("score", [])

         if score_list:
            score = score_list[0]
            runs = score.get("r")
            wickets = score.get("w")
            overs = score.get("o")
            inning = score.get("inning")

            print(f" {match_name} ({match_type})")
            print(f"Status: {status}")
            while(true):
                print(f"{inning}: {runs}/{wickets} in {overs} overs")
                time.sleep(30)
                break  # stop after finding first India match

