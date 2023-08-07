def expand_lists(nested_list):
    result = []
    
    for item in nested_list:
        if isinstance(item, list):
            result.extend(expand_lists(item))  
        else:
            result.append(item)
    
    return result

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17 , 18]]]
flattened_list = expand_lists(nice_list)
print(flattened_list)  