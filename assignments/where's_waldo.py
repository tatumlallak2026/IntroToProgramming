with open("C:\\Users\\tatum\\OneDrive\\Documents\\intro to programming\\IntroToProgramming\\assignments\\names.txt", "r") as file:
    
    found = False

    for lines in file:

        if (lines.strip() == "waldo"):
            found = True
            break

    if found:
         print("waldo was found!!")
         

    else:
        print("waldo is not here. . . ")

