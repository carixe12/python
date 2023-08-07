with open('numbers.txt', 'r') as f:
    numbers = f.read().split()

numbers = [int(num) for num in numbers]
total = sum(numbers)

with open('answer.txt', 'w') as f:
    f.write(str(total))