import json
json_str='{"name " : "francis","age":25,"city":"new york"}'
data=json.loads(json_str);
print(data)
print(type(data))
