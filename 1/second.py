def sum_of_digits(n):

    digit_sum = 0
    for digit in str(n):
        digit_sum += int(digit)
    return digit_sum


def count_digits(n):
    
    return len(str(n))


n = int(input("Enter number: "))
digit_sum = sum_of_digits(n)
digit_count = count_digits(n)
answer = digit_sum - digit_count

print(f"\nSum of numbers: {digit_sum}")
print(f"Number of digits in number: {digit_count}")
print(f"Difference between sum and number of digits: {answer}")