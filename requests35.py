import requests 
r=requests.get('https://www.google.com')
print(r.status_code)

url = "https://www.amazon.com/nothing_here"
try: 
    r=requests.get(url,timeout=1)
    r.raise_for_status()
except requests.exceptions.HTTPError as errh:
     print("HTTP Error")
     print(errh.args[0])

print(r)

url = "https://www.google.com"
try:
    r=requests.get(url,timeout=1)
    r.raise_for_status()
except requests.exceptions.RequestException as eerex:
    print("exception request")
