num_skates = int(input("Number of skates: "))
skate_sizes = []
for i in range(num_skates):
    size = int(input(f"Pair size {i+1}: "))
    skate_sizes.append(size)
    
num_people = int(input("Number of people: "))
foot_sizes = []
for i in range(num_people):
    size = int(input(f"Human foot size {i+1}: "))
    foot_sizes.append(size)

max_pairs = 0
for foot_size in foot_sizes:
    for i, skate_size in enumerate(skate_sizes):
        if skate_size >= foot_size:
            max_pairs += 1
            skate_sizes.pop(i)
            break

print(f"Most people who can borrow skates: {max_pairs}")