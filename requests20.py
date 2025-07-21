import requests
response=requests.get("https://api.github.com/")
print(response.cookies)
res=requests.get("https://www.google.com/")
print(res.cookies)
