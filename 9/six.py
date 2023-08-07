import zipfile
from collections import Counter
import string

with zipfile.ZipFile('voina-i-mir.zip', 'r') as zip_ref:
    zip_ref.extractall()

with open('tolstoy-war-and-peace.txt', 'r', encoding='utf-8') as f:
    text = f.read()

counted_chars = Counter(text)
total_chars = sum(counted_chars.values())
english_letters = string.ascii_lowercase + string.ascii_uppercase

print(f"{'Character':<10}{'Count':<10}{'Frequency':<12}")
for char, count in counted_chars.most_common():
    if char in english_letters or char in string.digits or char in string.punctuation:
        frequency = count / total_chars
        print(f"{char:<10}{count:<10}{frequency:.6f}")