'''AUTHOR:GANESH
30/11/24
'''
def count(sentence):
    upper_case=0
    lower_case=0
    digits=0
    spaces=0
    sl=list(sentence)
    for letter in sl:
        if letter.isupper():
            upper_case+=1
        elif letter.islower():
            lower_case+=1
        elif letter.isdigit():
            digits+=1
        else:
            spaces+=1
    print("No Of Upper case letters", upper_case)
    print("No of Lower Case Letters", lower_case)
    print("no fo spaces",spaces)
    print("no of numbers",digits)

sentence=input("ENTER A SENTENCE: ")
count(sentence)