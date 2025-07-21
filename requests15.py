import requests
r=requests.get('https://jsonplaceholder.typicode.com/posts')
if 'application/json' in r.headers['Content-Type']:
    print(r.json())
else :
    print("not json")
