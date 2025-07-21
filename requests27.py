import requests
import json
r=requests.get("https://jsonplaceholder.typicode.com/posts/1")
data=json.loads(r.text)
print(data)

r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
r.encoding = 'utf-8'
print(r.text)
