import random

numbers = [random.randint(0, 99) for _ in range(10)]

pairs = [(numbers[i], numbers[i+1]) for i in range(0, len(numbers), 2)]

print("Original List:", numbers)
print("New list:", pairs)