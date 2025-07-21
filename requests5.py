import requests

r = requests.post('https://httpbin.org/post', data ={'key':'value'})

print(r.status_code)

print(r.json())
