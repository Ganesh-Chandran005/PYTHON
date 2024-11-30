'''AUTHOR:GANESH
30/11/24
'''
def mobile_no_check(a):
    if len(a)==10 and a[0] in "789":
        print("Your phone no",mobile_no,"Is Valid")
    else:
        print("Invalid mobile number")

mobile_no=input("enter a number")
mobile_no_check(mobile_no)