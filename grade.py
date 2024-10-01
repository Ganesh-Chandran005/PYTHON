'''AUTHOR:GANESH'''
'''This programme helps user to find the  grade of a student according to their overall mark'''
name=input("enter the name of the student")
roll_no=int(input("enter the roll number of the student"))
'''collecting the marks of all 5 subjects '''
print("PLEASE ENTER THE MARKS OUT OF 100")
math=int(input("maths marks"))
phy=int(input("physics marks"))
chem=int(input("chemistry marks"))
comp=int(input("computer marks"))
eng=int(input("english marks"))
'''calculating overall'''
overall=math+phy+chem+comp+eng
'''CALCULATING GRADE'''
if overall>=450:
    print("A1 GRADE")
elif overall>=350 and overall<=450:
    print("A GRADE")
elif overall>=250 and overall<=350:
    print("B GRADE")
elif overall<250:
    print("YOU ARE A FAILURE")
else:
    print("NOT PROMOTED")


