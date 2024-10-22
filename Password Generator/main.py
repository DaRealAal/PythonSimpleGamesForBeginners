import random

chars = "abcdefghiklmnopurstuvwsyuz"
chars_lower = chars.lower()
numbers = "1234567890"
chars_symb = "!@#$%^&*()"

char, num, symb, lower = True, True, True, True

pw = []

if char:
    pw += chars

if num:
    pw += numbers

if symb:
    pw += chars_symb

if lower:
    pw += chars_lower

length = 16
amount = 5

for password in range(amount):
    result = ''.join(random.sample(pw, length))
    print(result)