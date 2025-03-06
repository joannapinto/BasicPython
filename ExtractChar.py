string = input("Enter a string: ")

if len(string) < 2:
    print("String is too short.")
else:
    result = string[:2] + string[-2:]
    print("Result:", result)
