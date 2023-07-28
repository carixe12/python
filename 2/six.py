elements = input("Enter the list of elements separated by space: ").split()

elements = [int(element) for element in elements]

k = int(input("Shift: "))

k = k % len(elements)

shifted_elements = elements[-k:] + elements[:-k]

print("Shifted list:", shifted_elements)