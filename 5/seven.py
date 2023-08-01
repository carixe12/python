ip = input("Enter IP: ")
parts = ip.split(".")

if len(parts) != 4:
    print("An address is four numbers separated by dots.")
else:
    for i in range(4):
        if not parts[i].isdigit():
            print("{} is not an integer.".format(parts[i]))
            break
        elif int(parts[i]) < 0 or int(parts[i]) > 255:
            print("{} is greater than 255.".format(parts[i]))
            break
    else:
        print("The IP address is correct.")