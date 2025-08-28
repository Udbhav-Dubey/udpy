import json
data={
    "name":"cody rhodes ",
    "roll no":94,
    "cgpa":8.6,
    "phone":"74846544645"
}
json_str=json.dumps(data,indent=4)
with open("sampl.json","w") as f:
    f.write(json_str)
