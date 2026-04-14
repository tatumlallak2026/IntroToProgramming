diameter = input("what is the diameter of the coin? ")
diameter = float(diameter)

if(diameter > 24.26):
    print("not a coin")
elif(diameter == 24.26):
    print("quarter")
elif(diameter == 21.21):
    print("nickel")
elif(diameter == 19.05):
    print("penny")
elif(diameter == 17.91):
    print("dime")
else:
    print("pocket lint...")