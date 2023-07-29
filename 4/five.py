s = input("Enter string: ")
first_h = s.find('h')
last_h = s.rfind('h')
substring = s[first_h:last_h]
reversed_substring = substring[::-1]
result = s[:first_h] + reversed_substring + s[last_h:]
print("Expanded sequence between the first and last h:", reversed_substring)