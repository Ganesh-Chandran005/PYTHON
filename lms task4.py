'''AUTHOR:GANESH
date:05-10-2024
Write a Python program that uses functions from the math module to perform the following operations on a number provided by the user:
'''
import math
number=int(input("enter a number:"))
sq=math.sqrt(number)
fac=math.factorial(number)
po=math.pow(number,2)
print("sqaure root of",number,"is:",sq)
print("factorial of",number,"is:",fac)
print(number,"raised to power 2 is:",po)