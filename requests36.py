import requests
url = "https://www.google.com"
try:
    r=requests.get(url,timeout=1)
    r.raise_for_status()
except requests.exception.ReadTimeout as errrt:
    print("time out")

print(r)

print("timeout : 0.1")
import requests
url = "https://www.google.com"
try:
    r=requests.get(url,timeout=0.1)
    r.raise_for_status()
except requests.exceptions.ReadTimeout as errrt:
    print("time out")

print(r)

