import random

def game():
    responce1 = input("wanna play a quick game of rock paper or scissors?")
    if responce1 == ("yes"):
        print("horay!")

    elif responce1 == ("no"):
        print("are you sure??")
        game()

    else: 
        print("please awnser yes or no")
        game()
