import itertools
a=[[1,2],[3,4],[5,6]]
b=itertools.chain(*a)
print([i for i in b])
