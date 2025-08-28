import json
geek='{"Name":"cody rhodes ","Languages":["python","c++","php"]}'
geek_dict=json.loads(geek)
print("dictionary after parsing : ",geek_dict)
print("\nvalues in languages : ",geek_dict["Languages"])
