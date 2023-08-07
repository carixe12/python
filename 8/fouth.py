def custom_sum(*args):
    total = 0
    
    for arg in args:
        if isinstance(arg, (list, tuple)):
            total += custom_sum(*arg)
        else:
            total += arg
    
    return total

print(custom_sum([[1, 2, [3]], [1], 3]))

