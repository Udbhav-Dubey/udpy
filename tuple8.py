list=[(0,10),(11,20),(21,30),(31,40),(41,50)]
print(list)
k=37
res=None
for idx ,ele in  enumerate(list):
    if k>=ele[0] and k<=ele[1]:
        res=idx;

print("the position is " + str(res))
