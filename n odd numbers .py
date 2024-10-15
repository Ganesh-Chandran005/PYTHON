'''AUTHOR:GANESH
15/10/2024
finding odd nummber in a user given limit'''
limit=int(input("enter a limit: "))
count=0
odd_number=1
while count<limit:
    print(odd_number,"\t",end="")
    count+=1
    odd_number+=2
