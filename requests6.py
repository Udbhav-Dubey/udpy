import requests 

data = {'name': 'Ud', 'city': 'Delhi'}
response=requests.post('https://httpbin.org/post',data=data)
print(response.json())
