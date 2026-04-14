def getnumber():
    n = input ("enter a number: ")
    try:
        n = float(n)
        print("you entered the number", n)
        return n
    except ValueError:
        print("invalid input, please enter a number")
        getnumber()

def Divide(n):
    try:
        return 10 /n
    except ZeroDivisionError:
        print("cannot divide by zero")

print(Divide(getnumber()))