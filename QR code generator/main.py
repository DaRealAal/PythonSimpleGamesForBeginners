import pyqrcode

https = 'https://'

user_enter = input("Enter a URL: ")

combine_link = https + user_enter

url = pyqrcode.create(user_enter)
print("")
url.svg('uca-url.svg', scale=8)
url.eps('uca-url.eps', scale=2)
print("Created:",combine_link)
print(url.terminal(quiet_zone=1))
