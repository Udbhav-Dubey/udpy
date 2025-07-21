import requests
payload = {'name': 'Ud', 'city': 'Delhi'}
r=requests.put("https://httpbin.org/put",data=payload)
print("status code :",r.status_code)
print("respinse body : ",r.content.decode())

