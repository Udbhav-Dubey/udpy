import requests

def get_live_scores():
    try:
        response = requests.get(url)
        data = response.json()

        if not data:
            print("No live matches at the moment.")
            return

        for match in data:
            print("="*40)
            print(f"🏏 {match['t1']} vs {match['t2']}")
            print(f"📍 Match: {match['match']}")
            print(f"🕒 Time: {match['time']}")
            print(f"📊 Score: {match['score']}")
            print("="*40)
            print()

    except Exception as e:
        print("⚠️ Error fetching data:", e)

if __name__ == "__main__":
    get_live_scores()

