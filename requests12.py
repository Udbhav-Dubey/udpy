import requests
r=requests.patch('https://httpbin.org/patch',data={'key':'value'})
print(r)
print(r.content.decode())
