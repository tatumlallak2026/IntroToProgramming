def get_number():
    num1 = int(input("Enter a number: "))
    try:
        n = int(num1)
    except ValueError:
        print("Invalid input. Please enter a valid number.")