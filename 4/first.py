text = input("Enter text: ")

vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
vowels_list = [char for char in text if char.lower() in vowels]

print("List of vowels:", vowels_list)
print("List length:", len(vowels_list))