import requests
r=requests.get('https://api.github.com/')
h=r.headers
print(h)
print()
print(h['Content-Type'])
print(h['Content-Length'])
print(h['Date'])
