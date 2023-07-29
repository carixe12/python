import string

message = input("Enter a message: ")
offset = int(input("Enter offset: "))

alphabet = string.ascii_lowercase
encrypted_message = ""

for letter in message:
    if letter.lower() in alphabet:
        index = (alphabet.index(letter.lower()) + offset) % len(alphabet)
        encrypted_message += alphabet[index]
    else:
        encrypted_message += letter

print("Encrypted message:", encrypted_message)