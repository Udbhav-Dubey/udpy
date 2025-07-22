import requests

response = requests.get('https://expired.badssl.com/', verify = False)

print(response)


print("manual")


response = requests.get('https://github.com/', verify ='/path / to / certfile')

print(response)
