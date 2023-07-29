nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17 , 18]]]

result = [num for inner_list in nice_list for nested_list in inner_list for num in nested_list]
print(result)