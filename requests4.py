import requests
r=requests.get("https://httpbin.org/html")
print(r)
print(r.content)
