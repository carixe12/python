def print_numbers(num, start=1):
    if start <= num:
        print(start)
        print_numbers(num, start + 1)
print_numbers(10)