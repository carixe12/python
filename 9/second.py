with open('zen.txt', 'r') as f:
    lines = f.readlines()

for line in reversed(lines):
    print(line.strip())