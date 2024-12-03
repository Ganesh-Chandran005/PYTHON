'''AUTHOR:GANESH
3/12/24
'''
import random
def monty(doors,items):
    r=random.choice(doors)
    s=random.choice(items)
    print("WELCOME TO MONTY HALL GAME!!")
    pick=int(input("Chose a door 1,2 or 3: "))
    if pick==1:
        host_pick=items[2]
        print("The host open the door,revealing a goat)
    elif pick==2:
        picked=items[1]
        host_pick=items[0]
        print("The host open the door 2,revealing a", host_pick)
    elif pick==3:
        picked=items[2]
        host_pick=items[0]
        print("The host open the door 2,revealing a", host_pick)
    choice=input("Do you want to switch your choice? (Yes/No):")
    if choice=="yes" and picked==1:
        picked=items[1]
    elif choice=="yes" and picked==2:
        picked=items[2]
    elif choice=="yes" and picked==3:
        picked=items[1]
    elif choice=="no":
        pass
    if picked==items[1]:
        print("Congratualtions! You have won the car")
        print("The car was behind the door",doors[1])
    else:
        print("The goat was revealed and You have lost")
        print("The car was behind the door",doors[1])


items=["goat","car","goat"]
doors=[1,2,3]
monty(doors,items)