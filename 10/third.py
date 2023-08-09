def validate_data(name, email, age):
    if not name or not email or not age:
        raise IndexError("All three fields are not present.")

    if not name.isalpha():
        raise NameError("The 'Name' field contains non-alphabetic characters.")

    if '@' not in email or '.' not in email:
        raise SyntaxError("The 'Email' field does not contain '@' and a dot.")

    age = int(age)
    if not (10 <= age <= 99):
        raise ValueError("The 'Age' field does not represent a number between 10 and 99.")

def process_data_line(line):
    try:
        name, email, age = line.split()
        validate_data(name, email, age)
        return line.strip()
    except (IndexError, ValueError, NameError, SyntaxError) as e:
        return line.strip() + "         " + str(e)

def main():
    registrations_good = []
    registrations_bad = []

    with open('registrations.txt', 'r') as file:
        for line in file:
            processed_line = process_data_line(line)
            if processed_line.count("         ") > 0:
                registrations_bad.append(processed_line)
            else:
                registrations_good.append(processed_line)

    with open('registrations_good.log', 'w') as file:
        file.write('\n'.join(registrations_good))

    with open('registrations_bad.log', 'w') as file:
        file.write('\n'.join(registrations_bad))

    print("Check completed. Please check 'registrations_good.log' and 'registrations_bad.log' files.")

if __name__ == '__main__':
    main()