first_number= input("Enter a first number")
second_number= input("Enter a second number")
result= float(second_number)-float(first_number)
if result>10:
    print("The result is greater than 10.")
elif result>0:
    print("The result is greater than 0 but not than 10.")
elif result==0:
    print("The result is zero.")
else:
    print("The result is a negative number.")
print("You can try again!")