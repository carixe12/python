def has_three_identical_digits(n):
    
    digit_count = [0] * 10
    for digit in str(n):
        digit_count[int(digit)] += 1
    return max(digit_count) == 3



a = int(input("Enter first year: "))
b = int(input("Enter second year: "))

print(f"\nYears from {a} to {b} with three identical digits:")
for year in range(a, b+1):
    if has_three_identical_digits(year):
        print(year)