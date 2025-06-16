import itertools
s1='''you stupid 
sob''' 

s2=''' idiot 
now enter the walls of jericho'''

s3='''you dont get it 
you just made the list '''

a=s1.splitlines();
b=s2.splitlines();
c=s3.splitlines();

result=[f"{line1} {line2} {line3}" for line1,line2,line3 in zip(a,b,c)]

for line in result:
    print(line)

result1 =map(lambda x:f"{x[0]} {x[1]} {x[2]}",zip(a,b,c))
for line in result:
    print(line)

result2 = [
    f"{line1} {line2} {line3}" 
    for line1, line2, line3 in itertools.zip_longest(a, b, c, fillvalue='')
]

for line in result:
    print(line)

