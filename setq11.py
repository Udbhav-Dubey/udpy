#Exercise 11: Set Intersection Check
#Write a code to check if two sets have any elements in common. If yes, display the common elements
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set3={110,120}
if set1.intersection(set2)!=None:
    print("set 1 and set2 have common")
if set2.intersection(set3)==None:
    print("set 2 and set 3 have nothing in common")
