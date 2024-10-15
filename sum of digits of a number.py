'''AUTHOR:GANESH
15/10/2024
sum of digits of a number'''
digit=int(input("enter a number"))
sum=0
while digit>0:
    r=digit%10
    sum=sum+r
    digit=digit//10
print(sum)