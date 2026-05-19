with open("C:\\Users\\tatum\\OneDrive\\Documents\\intro to programming\\IntroToProgramming\\assignments\\names.txt", "r") as file:
    
    found = False
    name = input("what name are you looking for? >>>").capitalize()
    x = 0 
    for lines in file:
        x += 1
        if (lines.strip() == name):
            found = True
            break

    if found:
         print( name, "was found on line", x)
         
    else:
        print(name, "is not here. . . ")

