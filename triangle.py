'''AUTHOR:GANESH
30/11/24
'''
def right_triangle(a,b,c):
    if b^2+a^2==c^2:
        print("This Triangle is a right triangle")
    else:
        print("Not a right triangle")




first_side=int(input("enter the length of the first side:"))
second_side=int(input("enter the length of the second side"))
third_side=int(input("enter the length of the third side"))
right_triangle(first_side,second_side,third_side)