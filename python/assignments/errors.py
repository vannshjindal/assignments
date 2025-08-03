#ZeroDivisionError – Division by Zero
def divide_numbers():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    except ValueError:
        print("Please enter valid numbers.")




#ValueError – Invalid Type Conversion
def convert_to_int():
    try:
        num = input("Enter a number: ")
        num = int(num)
        print("Integer value is:", num)
    except ValueError:
        print("That’s not a valid number.")




#IndexError – Accessing Out-of-Range List Index
def access_list_element():
    try:
        my_list = [10, 20, 30, 40]
        index = int(input("Enter index (0-3): "))
        print("Value at index:", my_list[index])
    except IndexError:
        print("Index out of range.")
    except ValueError:
        print("Please enter a number.")



#FileNotFoundError – Missing File
def read_file():
    try:
        filename = input("Enter filename to read: ")
        with open(filename, "r") as file:
            print("File content:\n", file.read())
    except FileNotFoundError:
        print("File not found.")




# TypeError – Invalid Operation on Data Types
def add_string_and_number():
    try:
        num = int(input("Enter a number: "))
        text = input("Enter some text: ")
        result = num + text  # Error: int + str
        print("Combined result:", result)
    except TypeError:
        print("You cannot add a number and a string.")
    except ValueError:
        print("Invalid number input.")
