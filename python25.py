l=["1","2","5","-2","5","6"]

print("sorted numerically:",
      sorted(l,key=lambda x: int(x)))

print("filtered positive even number : ",
      list(filter(lambda x : (int(x)%2==0 and int(x)>0),l)))

print("operation on each item using lambda and map()",
        list (map(lambda x:str(int(x)+10),l)))
