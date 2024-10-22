# Odd and even numbers


user_entered = int(input("Enter a range number to see if it's odd/even: "))


for num in range(0, user_entered, + 1):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


