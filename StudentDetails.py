'''AUTHOR:GANESH CHANDRAN'''


''' COLLECTING THE DETAILS OF A STUDENT'''
name=input("enter your name of the student:")
roll_number=int(input("enter the roll number of the student:"))
cgpa=float(input("Enter the CGPA of the student:"))

'''CALCULATING PERCENTAGE MARKS WITH A STUDENT'S CGPA'''
percentage_marks=cgpa*10


'''PRINTING ALL THE DETAILS'''
print("Name of the Student:",name)
print("Roll number of the Student:",roll_number)
print("CGPA of the student:",cgpa)
print("Percentage of the student:",percentage_marks,"%")

