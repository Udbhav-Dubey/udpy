import requests
r=requests.head("https://httpbin.org/",data={'key':'value'})
print(r)
print(r.headers)
print(r.content)
