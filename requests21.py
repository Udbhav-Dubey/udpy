import requests
response=requests.get("https://www.google.com/")
print(response)
print(response.history)
print(response.is_permanent_redirect)
print(response.is_redirect)
