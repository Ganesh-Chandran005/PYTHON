'''AUTHOR:GANESH
02/12/24'''
def multiply(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multiply(n1,n2-1)
print(multiply(5,3))
