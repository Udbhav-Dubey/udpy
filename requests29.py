import requests
res=requests.get("https://example.com/invalid")
print(res.raise_for_status)
res = requests.get('https://api.github.com/')
res.raise_for_status()
print("Success!")
try:
    res = requests.get('https://example.com/bad-url')
    res.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("HTTP error occurred:", e)
except requests.exceptions.RequestException as e:
    print("A request error occurred:", e)
res = requests.get('https://www.geeksforgeeks.org/naveen/')
res.raise_for_status()
