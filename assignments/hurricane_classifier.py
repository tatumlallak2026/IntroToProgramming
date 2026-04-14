def getspeed():
    try:
        speed = int(input("Enter the wind speed in miles per hour: "))
        if speed < 0:
            print("Speed cannot be negative. Please enter a valid speed.")
            return getspeed()
        return speed
    except ValueError:
        print("Invalid input, please enter a number.")
        return getspeed()
    
def classify():
    speed = getspeed()

    if speed < 74:
        print("The hurricane category is: Tropical Storm")
    elif speed >= 74 and speed <= 95:
        print("The hurricane category is: Category 1")
    elif speed >= 96 and speed <= 110:
        print("The hurricane category is: Category 2")
    elif speed >= 111 and speed <= 129:
        print("The hurricane category is: Category 3")
    elif speed >= 130 and speed <= 156:
        print("The hurricane category is: Category 4")
    else:
        print("The hurricane category is: Category 5")

classify()