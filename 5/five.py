import re

while True:
    password = input("Create a password: ")
    if len(password) < 8:
        print("The password is not secure. Try again.")
        continue
    if not re.search("[A-Z]", password):
        print("The password is not secure. Try again.")
        continue
    if len(re.findall("\d", password)) < 3:
        print("The password is not secure. Try again.")
        continue
    print("This is a strong password.")
    break