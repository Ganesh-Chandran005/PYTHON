'''AUTHOR:GANESH
2/12/24
'''

def fibonacci(n):
    sequence=[]
    first_number,second_number=0,1
    for i in range(n):
        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence
limit=int(input("Enter a limit:"))
print(fibonacci(limit))


