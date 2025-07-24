import requests

API_KEY = "c67ed518-9f52-4320-ba9f-561e18d7ce6b"
BASE_URL = "https://api.cricapi.com/v1"

def get_live_matches():
    url = f"{BASE_URL}/currentMatches"
    params = {"apikey": API_KEY}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()

def format_score(score_data):
    if not score_data or not isinstance(score_data, list):
        return "No score yet"
    
    formatted = []
    for s in score_data:
        runs = s.get('r')
        wickets = s.get('w')
        overs = s.get('o')
        inning = s.get('inning', "Inning")
        formatted.append(f"{inning}: {runs}/{wickets} in {overs} overs")
    return "\n　".join(formatted)

def main():
    data = get_live_matches()
    matches = data.get("data", [])
    if not matches:
        print("No live matches right now.")
        return

    found = False
    for m in matches:
        team1 = m.get("team-1") or "Unknown"
        team2 = m.get("team-2") or "Unknown"

        if "India" in (team1, team2):
            match_type = m.get("type", "")
            status = m.get("status", "")
            score = format_score(m.get("score"))

            print(f"🏏 {team1} vs {team2} ({match_type})")
            print(f"　Score:\n　{score}")
            print(f"　Status: {status}")
            print("-" * 40)
            found = True
            break  # remove if you want to see ALL India matches

    if not found:
        print("No live India match right now.")

if __name__ == "__main__":
    main()

