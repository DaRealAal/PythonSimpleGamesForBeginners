# cool text awesome

import random

special_symb = ['!', '@', '#', '$', '%', '&', '*', '-']
space = ' '


persons_word = input("Enter a word to print: ")

persons_choice = input("What would you like to do(space, special, upper): ")

if persons_choice == 'space':
    result1 = space.join(persons_word)
    for chars in result1:
        print(chars)
elif persons_choice == 'special':
    random_special = random.choice(special_symb)
    result2 = random_special.join(persons_word)
    for chars in result2:
        print(chars)
elif persons_choice == 'upper':
    upper_word = persons_word.upper()
    result3 = upper_word.join(persons_word)
    for char in upper_word:
        print(char)
else:
    print("Please enter only list(space, special, upper)")