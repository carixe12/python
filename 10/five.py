import math

def calculate_square_root(number):
    try:
        if number < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        result = math.sqrt(number)
        return result
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")

# Example usage
number = float(input("Enter a number: "))
square_root = calculate_square_root(number)
if square_root is not None:
    print(f"The square root of {number} is: {square_root}")