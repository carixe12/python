menu = input("Available menu: ")
menu_items = menu.split(";")
menu_items = [item.strip() for item in menu_items]
menu_string = ", ".join(menu_items)
print("Now the menu has:", menu_string)