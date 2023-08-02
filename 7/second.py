def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def crypto(iterable):
    return [element for idx, element in enumerate(iterable) if is_prime(idx)]

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# Output: [2, 3, 5, 7]

print(crypto('Brave New World!'))
# Output: ['d', 'i', 'n', 'd', 'v', 'd', 'r']