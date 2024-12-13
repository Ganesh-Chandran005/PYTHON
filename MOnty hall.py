'''AUTHOR:GANESH
'''


import random


def game_monty_hall():
    door_list = ['1', '2', '3']
    gift_list = ["car", "goat", "goat"]
    random.shuffle(gift_list)

    print(f"Welcome to the Monty Hall Game!")
    choice = input("Choose a door (1, 2, or 3): ")

    if choice not in door_list:
        print("Invalid choice!")
        return


    remaining_doors = [door for door in door_list
                       if door != choice]


    door_with_goat = remaining_doors[gift_list[door_list.index(remaining_doors[0])] == "goat"]

    print(f"Host opens door {door_with_goat}, revealing a goat.")


    switch = input("Do you want to switch to the remaining door? (yes/no): ").lower()

    if switch == "yes":
        final_choice = [door for door in door_list if door != choice and door != door_with_goat][0]
    else:
        final_choice = choice


    if gift_list[door_list.index(final_choice)] == "car":
        print(f"Congratulations! You won a car by choosing door {final_choice}!")
    else:
        print(f"Sorry! You got a goat. The car was behind door {door_list[gift_list.index('car')]}.")


game_monty_hall()