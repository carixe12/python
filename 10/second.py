import random

def write_to_file(number):
    with open('out_file.txt', 'a') as file:
        file.write(str(number) + '\n')

def main():
    total = 0
    while total < 777:
        try:
            num = int(input("Enter number: "))
            write_to_file(num)
            total += num
            if total >= 777:
                print("You have successfully completed the condition to exit the vicious cycle!")
        except Exception as e:
            if random.randint(1, 13) == 1:
                print("An exception occurred. Exiting the program.")
                return
            else:
                print("Invalid input. Please enter a valid number.")

    print("\nOut_file.txt file content:")
    with open('out_file.txt', 'r') as file:
        print(file.read())

if __name__ == '__main__':
    main()