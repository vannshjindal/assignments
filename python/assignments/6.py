text = input("Enter a sentence: ")
count = 1
for ch in text:
    if ch == ' ':
        count += 1
print(count)
