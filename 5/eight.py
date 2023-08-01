string1 = input("First line: ")
string2 = input("Second line: ")

if len(string1) != len(string2):
    print("The strings are not the same length.")
else:
    for i in range(len(string1)):
        if string1 == string2:
            print("The first line is obtained from the second with a shift of {}.".format(i))
            break
        string2 = string2[-1] + string2[:-1]
    else:
        print("The first row cannot be obtained from the second using a circular shift.")