import numpy as np
gfg=np.matrix('[64,1;12,3]')
print(gfg)
gfg.resize((1,4))
print("after resize:")
print(gfg)
gfg = np.matrix('[1, 2; 4, 5; 7, 8]')
geeks = gfg.resize((2, 3))
print(geeks)
