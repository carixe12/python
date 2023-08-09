def process_file(filename):
    total_characters = 0
    error_lines = []
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        for i, line in enumerate(lines, start=1):
            line = line.strip()
            line_length = len(line)
            
            if line_length < 3:
                error_lines.append(i)
            else:
                total_characters += line_length
        
    return total_characters, error_lines


def main():
    input_file = "people.txt"
    output_file = "errors.log"

    total_characters, error_lines = process_file(input_file)

    if error_lines:
        with open(output_file, 'w') as file:
            for line_number in error_lines:
                file.write(f"Error: less than three characters on line {line_number}.\n")

    print("Total number of characters:", total_characters)


if __name__ == "__main__":
    main()