import numpy as np
print(np.char.lower(['GEEKS',"LoWEr"]))
print(np.char.lower('SINGLe'))
print(np.char.split("geeks for geeks"))
print(np.char.split("geeks:for:geeks",sep=":"))
print(np.char.join('-','geeks'))
print(np.char.join(['-',':'],['geeks','for']))
