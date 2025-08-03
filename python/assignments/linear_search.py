numbers = [8, 3, 5, 2, 9, 1]
target = int(input("Enter number to search: "))

found = False
for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not found")
