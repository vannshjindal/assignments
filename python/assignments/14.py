n = int(input("Enter N: "))
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
