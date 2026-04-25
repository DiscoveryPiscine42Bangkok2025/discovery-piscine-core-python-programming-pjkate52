num = input("Give me a number: ")

if not float(num).is_integer():
    print("This number is a decimal.")
else:
    print("This number is an integer.")
