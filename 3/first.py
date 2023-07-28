a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a += b

num_fives = a.count(5)
a = [elem for elem in a if elem != 5]

a += c

num_threes = a.count(3)
print("Number of digits 5 on first concatenation:", num_fives)
print("Number of 3 digits on second concatenation:", num_threes)
print("Final list:", a)