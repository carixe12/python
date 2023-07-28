n = int(input("Enter number: "))


odd_numbers = []

for i in range(1, n+1):
    
    if i % 2 != 0:
        
        odd_numbers.append(i)


print("List of odd numbers from one to N:", odd_numbers)