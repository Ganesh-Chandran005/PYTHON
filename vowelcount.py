'''AUTHOR:GANESH
29/10/2024
To count the vowels of a sentence'''
str=input("enter a string")
vcount=0
for a in str:
    if a in "AEIOUaeiou":
        vcount+=1
        print(a,end="  ")
print(vcount)