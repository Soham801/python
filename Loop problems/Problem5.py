# Asking the user for input until they enter a value between 1 and 10.


while True:
    number = int (input("Enter a number Between 1 and 10 : "))
    if 1 <= number <= 10:
        print("Loop Successful")
        break
    else:
        print("Invalid Number , Try Again ")
    