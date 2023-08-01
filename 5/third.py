filename = input("File name: ")

if filename[0] in "@#$%^&*(":
    print("Error: The name starts with an invalid character.")
elif not filename.endswith(".txt") and not filename.endswith(".docx"):
    print("Error: Invalid file extension. Expected .txt or .docx.")
else:
    print("The file is named correctly.")