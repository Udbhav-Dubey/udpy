import requests
r=requests.delete('https://httpbin.org/delete',data={'key':'value'})
print(r.status_code)
print(r.json())
