'''AUTHOR:GANESH
3/12/24'''

def add_num(x,y):
    if y==0:
        return x
    else:
        return add_num(x+1,y-1)
n=add_num(5,3)
print(n)