import random

num = random.randrange(1,100)
guess = 0 

while guess != num:
    try:
        guess = int(input("whats your guess?\n>"))

    except:
        print("please enter a valid number")
        continue
        if guess == num:
            print("you win!")

        elif guess < num:
            print("too low")

        elif guess > num:
            print("too high")

    

print("finished")