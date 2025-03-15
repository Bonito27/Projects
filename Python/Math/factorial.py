#This code calculates the factorial of a number
while True:
    try:
       number = int(input("Please enter the number you want to find the factorial of!"))

       result = 1 

       while number > 0:
            result = result * number
            number -= 1

       print(f"The factorial of this number is: {result}")
    except ValueError:
        print("Invalid input! Plase enter a valid number!")


