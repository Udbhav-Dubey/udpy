import requests 
url = "www.google.com"
try:
    r = requests.get(url, timeout=1)
    r.raise_for_status()
except requests.exceptions.MissingSchema as errmiss:
    print("Missing schema: include http or https")
except requests.exceptions.ReadTimeout as errrt:
    print("Time out")
