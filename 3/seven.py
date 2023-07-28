n = int(input("Number of people: "))
k = int(input("What is the number in the counter? "))

people = list(range(1, n+1))
pos = 0
while len(people) > 1:
    pos = (pos + k - 1) % len(people)
    print(f"Person number {people[pos]} is eliminated")
    people.pop(pos)
print(f"The last person standing is number {people[0]}")