n = int(input("Number of numbers: "))
seq = []
for i in range(n):
    num = int(input("Number: "))
    seq.append(num)
num_needed = 0
nums_to_add = []
if seq == seq[::-1]:
    print("Sequence is already symmetrical")
else:
    for i in range(n):
        prefix = seq[:i+1]
        suffix = seq[::-1][:i+1][::-1]
        if prefix == suffix:
            num_needed = n - len(prefix)
            nums_to_add = seq[-num_needed:][::-1]
            break

    print(f"Need to add {num_needed} numbers to make the sequence symmetrical")
    print(f"The numbers themselves: {nums_to_add}")