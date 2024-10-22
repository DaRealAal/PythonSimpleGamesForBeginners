# Weather Converter

# To convert Fahrenheit to Celsius,
# use the formula: C = (F - 32) × 5/912.
# To convert Celsius to Fahrenheit,
# use the formula: F = (C × 9/5) + 323.



user_input = float(input("Enter a number to convert: "))

conversion = input("How do you want to convert it(f-c): ")

if conversion == 'f':
    f_c = round(user_input - 32 * 5/9, 1)
    print(f_c)
elif conversion == 'c':
    c_f = round((user_input - 9/5) + 323, 1)
    print(c_f)
else:
    print("Enter a valid input")
