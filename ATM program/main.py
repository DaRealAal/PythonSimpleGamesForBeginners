import time

balance = 0
is_running = True


while is_running:

    def show_balance():
        global balance

        print("***********************")
        print(f"* Balance: {balance:.2f} *")
        print("***********************")

    def withdraw():
        amount = float(input("Enter a withdraw: "))
        if amount > balance:
            print("Insufficient funds")
            return 0
        else:
            return amount

    def deposit():
        amount = float(input("Enter a deposit: "))
        if amount < 0 :
            print("Insufficient funds")
            return 0
        else:
            return amount

    print("Welcome to the ATM Program!")
    print("1. Show Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    user_input = input("What do you want to do(1-4)? ")

    

    if user_input == '1':
        print("Please wait...")
        time.sleep(1)
        show_balance()
    elif user_input == '2':
        print("Please wait...")
        time.sleep(3)
        balance -= withdraw()
    elif user_input == '3':
        print("Please wait...")
        time.sleep(3)
        balance += deposit()
    elif user_input == '4':
        print("Thank you! have a great day.")
        is_running = False