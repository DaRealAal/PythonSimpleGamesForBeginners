# Weight converter

try:
    weight = float(input("Enter your weight: "))
    convert = input("How do you want to convert your weight?(k - l: )")
    if convert == 'k':
        result = weight * 2.2046
        print(f"Your weight {weight:.2f}")
        print(f"Your converted weight: {result:.2f}")
    elif convert == 'l':
        result = weight / 2.2046
        print(f"Your weight {weight:.2f}")
        print(f"Your converted weight: {result:.2f}")
    else:
        print(f"{weight:.2f} is not a valid option")
except ValueError:
    print("Enter only number please!")