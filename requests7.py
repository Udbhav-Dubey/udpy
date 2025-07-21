import requests 

payload = {'name': 'Ud', 'city': 'Delhi'}
response = requests.post('https://httpbin.org/post', json=payload)
print(response.json())
