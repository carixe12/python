import string

with open('text.txt', 'r') as f:
    text = f.read()

english_letters = string.ascii_lowercase
letter_counts = {letter: 0 for letter in english_letters}
total_count = 0

for char in text:
    if char.lower() in english_letters:
        letter_counts[char.lower()] += 1
        total_count += 1

letter_proportions = {letter: count/total_count for letter, count in letter_counts.items() if count > 0}
sorted_proportions = sorted(letter_proportions.items(), key=lambda x: (-x[1], x[0]))

with open('analysis.txt', 'w') as f:
    for letter, proportion in sorted_proportions:
        f.write(f"{letter} {proportion:.3f}\n")