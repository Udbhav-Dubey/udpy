import json
data={
    "name":"cody rhodes",
        "roll no":56,
    "cgpa":5.4,
    "phone":"1231231231"
}
with open("sample.json","w") as f:
    json.dump(data,f)
