import os

def get_directory_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_directory_size(entry.path)
    return total

def count_files_and_directories(path='.'):
    num_files = 0
    num_dirs = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                num_files += 1
            elif entry.is_dir():
                num_dirs += 1
                sub_files, sub_dirs = count_files_and_directories(entry.path)
                num_files += sub_files
                num_dirs += sub_dirs
    return num_files, num_dirs

directory_path = input("Enter directory path: ")
size_kb = get_directory_size(directory_path) // 1024
num_files, num_dirs = count_files_and_directories(directory_path)

print(f"Directory size (in KB): {size_kb}")
print(f"Number of subdirectories: {num_dirs}")
print(f"Number of files: {num_files}")