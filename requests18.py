import requests
response=requests.get("https://www.google.com")
print(response)
print(response.elapsed)
response.close()
print("response closed")
