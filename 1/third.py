def smallest_divisor(n):
    
    for i in range(2, n+1):
        if n % i == 0:
            return i
    return None


n = int(input("Enter number: "))
divisor = smallest_divisor(n)

if divisor is None:
    print("No non-one divisor found.")
else:
    print(f"\nSmallest non-one divisor: {divisor}")