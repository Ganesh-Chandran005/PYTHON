'''AUTHRO:GANESH
15/10/2024
TO FIND ENTRY FARE ACCORDING TO AGE'''
age=int(input("enter your age"))
if age<10:
    fare=7
elif age>=10 and age<60:
    fare=10
else:
    fare=5
print("Entry fare is",fare)