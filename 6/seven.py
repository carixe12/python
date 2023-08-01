array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

common_elements = []
for element in array_1:
    if element in array_2 and element in array_3:
        common_elements.append(element)
print("Task 1 - Without sets:", common_elements)

# With sets
set_1 = set(array_1)
set_2 = set(array_2)
set_3 = set(array_3)
common_elements_set = set_1.intersection(set_2, set_3)
print("Task 1 - With sets:", list(common_elements_set))

unique_elements = []
for element in array_1:
    if element not in array_2 and element not in array_3:
        unique_elements.append(element)
print("Task 2 - Without sets:", unique_elements)

unique_elements_set = set_1.difference(set_2, set_3)
print("Task 2 - With sets:", list(unique_elements_set))