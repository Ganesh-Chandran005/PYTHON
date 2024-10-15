'''AUTHOR:GANESH
15/10/2024
FINDING SMALLEST OF THREE NUMBERS'''

n1=int(input("enter a number"))
n2=int(input("enter a nummber"))
n3=int(input("enter a number"))
if n1<n2 and n1<n3:
    print(n1,"is the smallest")
elif n2<n1 and n2<n3:
    print(n2,"is the smallest")
elif n3<n2 and n3<n1:
    print(n3,"is the smallest")
else:
    print("all number are equal")