import random

user_roll = input("Enter a y to roll a dice or q to quit: ")

dices = random.randrange(1,7)
while True:
    if user_roll == 'y':
        print("dice", dices)
        break
    elif user_roll == 'q':
        break