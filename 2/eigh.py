
numbers = input("Enter the list of numbers separated by space: ").split()

numbers = [int(number) for number in numbers]

for i in range(len(numbers)):
    
    min_index = i
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j
    
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("Sorted list:", numbers)