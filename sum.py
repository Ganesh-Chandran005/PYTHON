'''AUTHOR:GANESH'''
''''This programme finds the sum of all the numbers between a specific limit given by the user'''
limit=int(input("enter a limit:"))
sum=0
for i in range(limit+1):
    if i!=0:
        sum=sum+i
print("The sum is",sum)
