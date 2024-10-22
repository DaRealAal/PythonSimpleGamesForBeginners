# Shopping order

fruits_list = []

while True:

    user_choice = input("Enter a list of fruits to add on your cart(type d to done): ")

    if user_choice == 'apple':
        fruits_list.append(user_choice)
    elif user_choice == 'banana':
        fruits_list.append(user_choice)
    elif user_choice == 'cherry':
        fruits_list.append(user_choice)
    elif user_choice == 'watermelon':
        fruits_list.append(user_choice)
    elif user_choice == 'orange':
        fruits_list.append(user_choice)
    elif user_choice == 'pear':
        fruits_list.append(user_choice)
    elif user_choice == 'kiwi':
        fruits_list.append(user_choice)
    elif user_choice == 'd'.lower():
        print("---------- CART ITEMS ----------")
        print(' ')
        print("Thank you for shopping with us!")
        print(' ')
        for index, list_print in enumerate(fruits_list, start=1):
            print(f"{index}. {list_print}")
        break
    else:
        print("This item is out of stock.")