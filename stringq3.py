#Exercise 3: Create a new string made of the first, middle, and last characters of each input string
s1 = "America"
s2 = "Japan"
mid1=int(0+(len(s1)-1)/2)
mid2=int(0+(len(s2)-1)/2)
s=s1[0]+s2[0]+s1[mid1]+s2[mid2]+s1[len(s1)-1]+s2[len(s2)-1]
print(s)
