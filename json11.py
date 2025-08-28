import json
import requests 
res = requests.get("http://dummy.restapiexample.com/api/v1/employees")
d=json.loads(res.text)
d=json.dumps(d)
print(d)
print(type(d))
