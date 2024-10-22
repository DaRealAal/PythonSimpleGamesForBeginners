# Benchmark Program PC
import random
import time

running = True

def start_benchmark():
    print("STARTING IN 10 SECOND:")
    print("PRESS CTRL + Z TO CANCEL THE BENCHMARK")
    for count_down in range(1, 10 + 1):
        print(count_down)
        time.sleep(1)
    while True:
        generating = random.randrange(1000, 9999, 10)
        print("Benchmarking:", generating)

def about():
    print("This software created by: Ali")
    print("and this might be yours:)")

def requirements():
    print("Any PC that has a CPU and a RAM in it.")

while running:
    print("Welcome to the PC Benchmark test")
    print("Select an option:")
    print("1. Start Benchmark Test")
    print("2. Requirements")
    print("3. About")
    print("4. Exit")
    user_input = input("Choose(1-4)> ")


    if user_input == '1':
        start_benchmark()
    elif user_input == '2':
        requirements()
    elif user_input == '3':
        about()
    elif user_input == '4':
        print("Have a great day!")
        running = False