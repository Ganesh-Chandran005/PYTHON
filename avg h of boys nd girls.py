'''AUTHOR:GANESH
15/10/2024
To find the average height of boys and girl in calss of n students'''
n=int(input("ener the number of student in a class"))
btotal=0
gtotal=0
tbh=0
tgh=0
for i in range(0,n+1):
    gender=input("enter your gender M/F")
    height=float(input("enter your height"))
    if gender=="M" or gender=="m":
        btotal+=1
        tbh=tbh+height
    else:
        gtotal+=1
        tgh=tgh+height

avg_bh=tbh/btotal
avg_gh=tgh/gtotal
print("Average height of boys",avg_bh)
print("Average height of girls",avg_gh)
