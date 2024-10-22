'''AUTHOR:GANESH
22/10/2024
Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit.
The user should be able to input a temperature in Celsius or Fahrenheit,
and the program should convert it to the other unit using the formula
'''
temp=float(input("Enter the temperature:"))
corf=input("Is This in (C)elsius or (F)ahrenheit?")
if corf=="C":
    c="Celsius"
else:
    c="Fahrenheit"
ctemp=0
if corf=="C":
    f="Fahrenheit"
    ctemp=(9/5*temp)+32
else:
    f="Celsius"
    ctemp=5/9*(temp-32)
print(temp," ",c,"is",ctemp,f)
