import requests
response=requests.get('https://api.github.com/')
print(response)
print(response.reason)
response = requests.get('https://www.geeksforgeeks.org/ / n/')

print(response)

print(response.reason)
