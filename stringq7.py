'''Exercise 7: String characters balance Test

Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.'''

s1=input("enter the s1 : ")
s2=input("enter the s2 : ")
flag=0
for i in s1:
    if (s2.find(i)==-1):flag=1;

if flag==1:print("not balanced")
else: print("balanced ")
