string = input("Enter a string: ")
words = string.split()

for i in range(len(words)):
    words[i] = words[i][0].upper() + words[i][1:].lower()

result = " ".join(words)
print("Result:", result)