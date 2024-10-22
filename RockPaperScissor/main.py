import random
is_running = True

while is_running:


    options = ['rock', 'paper', 'scissor']
    player = ''
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a (rock, paper, scissor): ")
        if player not in options:
            print("please enter valid input")

    print("Player:", player)
    print("Computer:", computer)

    if player == computer:
        print("Tie!")
    elif player == 'rock' and computer == 'paper':
        print("you win!")
    elif player == 'scissor' and computer == 'rock':
        print("you lose!")
    elif player == 'paper' and computer == 'scissor':
        print("you lose!")
    elif player == 'rock' and computer == 'scissor':
        print("you win!")



    play_again = input("Do you wanna play again(y/n): ").lower()

    if play_again != 'y':
        is_running = False



