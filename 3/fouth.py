guests = ['Petya', 'Vanya', 'Sasha', 'Lisa', 'Katya']

while True:
    print(f"Now there are {len(guests)} people at the party: {guests}")
    action = input("Did the guest come or go? ").strip().lower()
    if action == "came":
        if len(guests) == 6:
            print("I'm sorry, but there are no places.")
        else:
            name = input("Guest Name: ")
            guests.append(name)
            print(f"Hi {name}!")
    elif action == "gone":
        name = input("Guest Name: ")
        if name in guests:
            guests.remove(name)
            print(f"So long, {name}!")
        else:
            print(f"I'm sorry, but {name} is not at the party.")
    elif action == "time to sleep":
        print("The party ended and everyone went to bed.")
        break
    else:
        print("Invalid input. Please enter 'came' or 'gone', or 'time to sleep' to end the party.")