def is_prime():
    num = int(input("Enter a number: "))
    if num < 2:
        print("Not a prime number")
        return
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            return
    print("Prime number")

def divisible_by_3_and_5():
    n = int(input("Enter N: "))
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)

def even_sum_1_to_100():
    total = 0
    for i in range(1, 101):
        if i % 2 == 0:
            total += i
    print("Sum is:", total)

def leap_year():
    year = int(input("Enter year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
    else:
        print("Not a leap year")

def factorial():
    num = int(input("Enter number: "))
    result = 1
    for i in range(1, num+1):
        result *= i
    print("Factorial is:", result)

def word_count():
    s = input("Enter a string: ")
    words = s.split()
    print("Word count:", len(words))

def largest_of_three():
    a = int(input("Enter first: "))
    b = int(input("Enter second: "))
    c = int(input("Enter third: "))
    if a >= b and a >= c:
        print("Largest:", a)
    elif b >= a and b >= c:
        print("Largest:", b)
    else:
        print("Largest:", c)

def day_of_week():
    num = int(input("Enter number (1-7): "))
    if num == 1:
        print("Monday")
    elif num == 2:
        print("Tuesday")
    elif num == 3:
        print("Wednesday")
    elif num == 4:
        print("Thursday")
    elif num == 5:
        print("Friday")
    elif num == 6:
        print("Saturday")
    elif num == 7:
        print("Sunday")
    else:
        print("Invalid")

def reverse_number():
    num = int(input("Enter number: "))
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    print("Reversed:", rev)

def vowel_or_consonant():
    ch = input("Enter a character: ").lower()
    if ch in "aeiou":
        print("Vowel")
    elif ch.isalpha():
        print("Consonant")
    else:
        print("Not a letter")

def multiplication_table():
    num = int(input("Enter number: "))
    for i in range(1, 11):
        print(num, "x", i, "=", num*i)

def check_sign():
    num = int(input("Enter number: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

def average_array():
    nums = input("Enter numbers: ").split()
    total = 0
    for n in nums:
        total += int(n)
    print("Average:", total / len(nums))

def fibonacci():
    n = int(input("How many terms: "))
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def char_type():
    ch = input("Enter a character: ")
    if ch.isalpha():
        print("Alphabet")
    elif ch.isdigit():
        print("Digit")
    else:
        print("Special character")

def month_season():
    month = int(input("Enter month number: "))
    if month in [12, 1, 2]:
        print("Winter")
    elif month in [3, 4, 5]:
        print("Spring")
    elif month in [6, 7, 8]:
        print("Summer")
    elif month in [9, 10, 11]:
        print("Autumn")
    else:
        print("Invalid")

def count_vowels():
    s = input("Enter a string: ")
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    print("Vowel count:", count)

def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+ - * /): ")
    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operator")

def greater_than_value():
    arr = list(map(int, input("Enter numbers: ").split()))
    x = int(input("Enter value: "))
    for i in arr:
        if i > x:
            print(i)

def is_palindrome():
    s = input("Enter a string: ")
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

def main():
    while True:
        print("\nSelect option (0 to exit):")
        print("1. Prime  2. Div by 3&5  3. Even sum  4. Leap Year")
        print("5. Factorial  6. Word Count  7. Largest of 3  8. Day of Week")
        print("9. Reverse Num  10. Vowel/Consonant  11. Table  12. Pos/Neg/Zero")
        print("13. Average  14. Fibonacci  15. Char Type  16. Season by Month")
        print("17. Count Vowels  18. Calculator  19. > Value  20. Palindrome")

        choice = input("Enter choice: ")

        if choice == '1':
            is_prime()
        elif choice == '2':
            divisible_by_3_and_5()
        elif choice == '3':
            even_sum_1_to_100()
        elif choice == '4':
            leap_year()
        elif choice == '5':
            factorial()
        elif choice == '6':
            word_count()
        elif choice == '7':
            largest_of_three()
        elif choice == '8':
            day_of_week()
        elif choice == '9':
            reverse_number()
        elif choice == '10':
            vowel_or_consonant()
        elif choice == '11':
            multiplication_table()
        elif choice == '12':
            check_sign()
        elif choice == '13':
            average_array()
        elif choice == '14':
            fibonacci()
        elif choice == '15':
            char_type()
        elif choice == '16':
            month_season()
        elif choice == '17':
            count_vowels()
        elif choice == '18':
            calculator()
        elif choice == '19':
            greater_than_value()
        elif choice == '20':
            is_palindrome()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
