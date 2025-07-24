import requests
import time

while True:
    try:
        r = requests.get("https://api.cricapi.com/v1/currentMatches?apikey=YOUR_API_KEY&offset=0")
        data = r.json()

        # example logic
        for match in data["data"]:
            if "India" in match.get("teams", []):
                print(f"\n{match['name']} ({match['matchType']})")
                print("Status:", match["status"])
                score = match.get("score", [])
                if score:
                    s = score[0]
                    print(f"{s['inning']}: {s['r']}/{s['w']} in {s['o']} overs")
                break

        time.sleep(30)

    except KeyboardInterrupt:
        print("Stopped.")
        break

