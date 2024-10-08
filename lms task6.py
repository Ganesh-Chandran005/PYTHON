'''AUTHOR:GANESH
08/10/2024
Simple desktop calculator using Python. Only the five basic arithmetic operators.'''
'''collecting numbers'''
num1=int(input("enter a number"))
num2=int(input("enter a number:"))
num3=int(input("enter a number:"))
'''ADDITION'''
sum=num1+num2
print("The sum of num1 and num2 is",sum)
'''SUBSTRACTION'''
diff=num2-num1
print("The difference when num2 is subtracted from num1 is:",diff)
'''MULTIPLICATION'''
mul=num1*num2
print("The product of num1 and num2 is:",mul)
'''DIVISION'''
if num2==0:
    print("divion by zero not possible")
else:
    div=num1/num2
    print("The quotient when num1 is divided by num2 is:",div)
'''MODULUS'''

if num2==0:
    print("Finding remainder with 0 not possible")
else:
    mod = num1 % num2
    print("The remainder when num1 is divided by num2 is:",mod)
'''COMBINED ARIHMETIC RESULT'''
result = (num1 + num2) * num3 / 2
print("The result of (num1 + num2) * num3 / 2 is:",result)



