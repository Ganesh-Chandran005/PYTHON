'''AUTHOR:GANESH
22/10/2024
Write a Python program to find the largest of three numbers.
The program should take three numbers as input from the user and determine which one is the largest.
Use conditional statements to compare the numbers.
'''
num1=int(input("Enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
lar=0
if num1>num2 and num1>num3:
    lar=num1
elif num2>num1 and num2>num3:
    lar=num2
elif num3>num1 and num3>num2:
    lar=num3
else:
    print("ALL NUMBERS ARE EQUAL")
print("Largest number is:",lar)