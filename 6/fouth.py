def invert_dict(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    return inverted_dict

text = input("Enter text: ")
freq_dict = {}
for char in text:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1
print("Original frequency dictionary:\n")
for key, value in sorted(freq_dict.items()):
    print(key, ":", value)

inverted_dict = invert_dict(freq_dict)

print("\nInverted frequency dictionary:\n")
for key, value in sorted(inverted_dict.items()):
    print(key, ":", value)