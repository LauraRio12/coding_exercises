secret_number="8"
secret_color="yellow"

your_number= input("Choose a number between 1 and 20")
your_color= input ("Choose a color from the rainbow")

if your_number=="8" and your_color=="yellow":
    print("You've found both the secret number and the secret color!")
elif your_number=="8" or your_color=="yellow":
    print("You found at least one of the secrets!")
else:
    print("You didn't find any of the secrets! and Better luck next time!")
    print("Better luck next time!")
print("Try again! ")