a = int(input("Enter your age : "))

if(a>18):
    print("Above the consent age")

elif(a<0):
    print("Enter a valid age")

elif(a==0):
    print("Age cannot be zero")

else:
    print("Below the consent age")



a1 = int(input("Enter 1 number: "))
a2= int(input("Enter 2 number: "))
a3 = int(input("Enter 3 number: "))


if(a1>a2 and a1>a3 ):
    print("the gratest number is : ", a1)
    
elif(a2>a1 and a2>a3 ):
    print("the gratest number is : ", a2)

elif(a3>a2 and a3>a1 ):
    print("the gratest number is : ", a3)

else:
    print("All the numbers are same.")



p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
message = input("Enter your comment : ")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("Spam message")


else:
    print("OK")



username = input("Enter your username : ")

if(len(username)>=10):
    print("You are good to go!")

else:
    print("the username should be above 10 letters")





marks = int(input("Enter the marks : "))


if(marks>100 or marks <0):
    print("Enter valid marks!")


if(marks >90 and marks<=100):
    print("Excellent")

elif(marks >80 and marks<=90):
    print("A")

elif(marks >70 and marks<=80):
    print("B")

elif(marks >60 and marks<=70):
    print("C")

elif(marks >50 and marks<=60):
    print("D")

elif(marks<50):
    print("Fail")

else:
    print("Enter correct marks")




message = input("Enter your message content : ")

if("harry" in message):
    print("Harry found in message content")


