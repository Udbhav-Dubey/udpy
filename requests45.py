import requests


def get_live_matches():
    url = f"{BASE_URL}/currentMatches"
    params = {"apikey": API_KEY}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()

def main():
    data = get_live_matches()
    matches = data.get("data", [])
    if not matches:
        print("No live matches right now.")
        return

    for m in matches:
        team1, team2 = m.get("team-1"), m.get("team-2")
        score = m.get("score", "No score yet")
        status = m.get("status", "")
        match_type = m.get("type", "")
        print(f"🏏 {team1} vs {team2} ({match_type})")
        print(f"　Score: {score}")
        print(f"　Status: {status}")
        print("-" * 40)

if __name__ == "__main__":
    main()

