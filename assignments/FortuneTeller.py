import random

def fortune_telling():
    print("welcome to the wimsical world of zandar the fortune teller!")
    def ask_for_age():
        
        age = input("please enter your age: ")
        try:
            age = int(age)
        except ValueError:
            print("age must be a number! please enter a valid age.")
            return ask_for_age()
        if age <= 0:
            print("age must be a positive WHOLE number! please enter a valid age.")
            return ask_for_age()
        return age
    age = ask_for_age()

    def ask_for_lucky_num():
        luk_num = input("please enter your lucky number: ")
        try:
            luk_num = int(luk_num)
            return luk_num
        except ValueError:
            print("lucky number must be a number! please enter a valid lucky number.")
            return ask_for_lucky_num()
        
    luk_num = ask_for_lucky_num()

    def FarFuture():
        future_years = input("how many years into the future would you like to see? ")
        try:
            future_years = int(future_years)
        except ValueError:
            print("future years must be a number! please enter a valid number.")
            return FarFuture()
        return future_years
    future_years = FarFuture()

    print("im starting to see something in the crystal ball...")

    def generate():
        return random.randrange(1, 50)

    gen = generate()

    def add_stuff():
        return int(age) + int(luk_num) + int(future_years) + int(gen)
    result = add_stuff()

    if result < 0:
        print("You need to be careful, you have a dark future ahead of you. . . ")

    elif result <= 25:
        print("keep working hard and you will achieve your dreams!")

    elif result <= 50:
        print("you have a bright future ahead of you, ")

    elif result == 67:
        def brainrot():
            print("67")
            brainrot()

    elif result <= 75:
        print("you will find love and settle down on a little farm. . .")

    elif result <= 100:
        print("you will become a millionaire and live in a mansion on the beach!")
    else:
        print("you will become a world famous celebrity and live in a mansion on the beach with your 1000 dogs!")

fortune_telling()