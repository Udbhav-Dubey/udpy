a={1,2,3,4,5,6,7,8}
print(str(a))
rem={6,7}
res=a-rem
print("new : ",res)
rem1={5,6}
a.difference_update(rem1)
print("new ",a)
rem2={3,4}
common=a.intersection(rem2)
a-=common
print("new ",a)
rem3={2,7,8}
a=set(filter(lambda x : x not in rem3,a))
print("new ",a)
