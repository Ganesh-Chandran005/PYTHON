'''AUTHOR:GANESH
2/12/24
'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))