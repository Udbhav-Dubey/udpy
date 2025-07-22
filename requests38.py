import requests
url="https://www.udbhav.dubey/"
try:
  r = requests.get(url, timeout = 1, verify = True)
  r.raise_for_status()
except requests.exceptions.HTTPError as errh:
  print("HTTP Error")
  print(errh.args[0])

except requests.exceptions.ReadTimeout as errrt:
  print("Time out")
except requests.exceptions.ConnectionError as conerr:
  print("Connection error")
