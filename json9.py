import json
from collections import OrderedDict
data=json.loads('{"GeeksforGeeks":1,"Gulshan":2,"nightfury_1":3,"Geek":4}',object_pairs_hook=OrderedDict)
print("ordered_dict: ",data)
