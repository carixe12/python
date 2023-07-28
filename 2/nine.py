
integers = input("Enter the list of integers separated by space: ").split()


integers = [int(integer) for integer in integers]

for i in range(len(integers)-1, -1, -1):
    if integers[i] % 2 == 0:
        print(integers[i])