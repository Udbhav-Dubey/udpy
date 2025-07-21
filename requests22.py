import requests
response=requests.get("https://www.google.com/")
print(response)
print(response.text)
print(response.iter_content())
for i in response.iter_content():
    print(i,end="  ")

