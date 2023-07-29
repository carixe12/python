n = int(input("Enter list length: "))

result = [(1 if i % 2 == 0 else i % 5) for i in range(n)]

print("Result:", result)

