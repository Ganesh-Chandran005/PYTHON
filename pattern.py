'''AUTHOR:GANESH
19-11-24'''

limit=int(input("enter a limit:"))
for i in range(0,limit):
    for j in range(i+1):
        print("*",end="")
    print()
print("  ")


for k in range(limit,0,-1):
    for p in range(k):
        print("*",end="")
    print()
print(" ")

for u in range(limit+1):
    for v in range(limit-u):
        print(" ",end=" ")
    for v in range(2*u-1):
        print("*",end=" ")
    print()

print(" ")

for u in range(limit,0,-1):
    for v in range(limit-u):
        print(" ",end=" ")
    for v in range(2*u-1):
        print("*",end=" ")
    print()

