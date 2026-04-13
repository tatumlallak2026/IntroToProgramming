x = input("Enter a number: ")
if int(x) >= 0:
    factorial = 1
    for i in range(1, int(x) + 1):
        factorial *= i
    print("Factorial of", x, "is", factorial)
else:
    print("Factorial is not defined for negative numbers.")
