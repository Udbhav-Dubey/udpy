import requests
response=requests.get('https://api.github.com/')
print("response : ",response)
print("encoding : ",response.encoding)
