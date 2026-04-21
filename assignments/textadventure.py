# setting-
# time: mid day like 3:00pm
# place: forest - warm summer day.
# mood: lost


def start_adventure():
    print("you wake up laying in the middle of a forest, you are lost with no memory of who you are, where you're from and how you got there.")
    print("you look around and see a dense forest all around. There is a rustic path that retreats into the dark canopy of the forest.")
    print("you turn around and see a small stream flowing.")
    print("you look left and see a another path that leads to an opening in the forest.")
    start_option()

def start_option():
    print("what should you do?")
    print("1. follow the rustic path")
    print("2. follow the stream")
    print("3. follow the path to the opening")
    print("4. stay where you are")
    int_input = input(">>>")

    if int_input == "1":
        rustic_path()

    elif int_input == "2":
        stream()

    elif int_input == "3":
        opening()

    elif int_input == "4":
        print("you stay right where you are. . .")
        print("nothing changes.")
        return_to_start()

    else:
        print("invalid input, try again.")
        start_option()

def return_to_start():
    print("everything looks the same, just the way you left it.")
    print("you feel a sense of deja vu.")
    print("what should you do?")
    print("1. follow the rustic path")
    print("2. follow the stream")
    print("3. follow the path to the opening")
    print("4. stay where you are")
    int_input = input(">>>")

    if int_input == "1":
        rustic_path()

    elif int_input == "2":
        stream()

    elif int_input == "3":
        opening()

    elif int_input == "4":
        print("you stay right where you are. . .")
        print("nothing changes.")
        return_to_start()

    else:
        print("invalid input, try again.")
        return_to_start()

def continue_in_tocave():
    print("against your own gut, you keep going. you continuously crawl through the canopy, often feeling small scratches on your skin.")
    print("after a while, your hands start to feel something sharp.")
    print("you keep feeling around, eveyrthing feels as if its made of stone.")
    print("you come to the conclusion that you are in a cave.")
    print("what do you do?")
    print("1. keep going")
    print("2. turn back")
    rusticpath2 = input(">>>")

    if rusticpath2 == "1":
            into_the_cave()

    elif rusticpath2 == "2":
            print("you turn back and head back to where you started.")
            return_to_start()

    else:
            print("invalid input, try again.")
            rustic_path()

def rustic_path():
    print("you follow the dark path, you duck your head into the canopy. light is ripped from your existence.")
    print("you are starting to have second thoughts.")
    print("what should you do?")
    print("1. keep going")
    print("2. turn back")
    rusticpath1 = input(">>>")

    if rusticpath1 == "1":
        continue_in_tocave()
                
    
    elif rusticpath1 == "2":
        print("you turn back and head back to where you started.")
        return_to_start()

    else:
        print("invalid input, try again.")
        rustic_path()

def endless_cave():
    print("you take another deep breath, and move forward about 10 more feet.")
    print("what do you do?")
    print("1. keep going")
    print("2. turn back")
    cave = input(">>>")

    if cave == "1":
        endless_cave()

    elif cave == "2":
        bad_cave_ending()
    
    else:
        print("invalid input, try again.")
        endless_cave()

def bad_cave_ending():
    print("you take another deep breath and start to crawl feet first")
    print("The sharp edges of the creves cut into your skin.")
    print("you start to panic, you try to move but you feel as if your body is being squeezed more and more the further you go back.")
    print("you are stuck. . .")
    print("YOUR JOURNEY HAS COME TO AN END, YOU ARE TRAPPED IN THE CAVE TILL THE END OF TIME.")

def into_the_cave():
    print("you continue into the cave, it feels if as if you body is being squeezed more and more the deeper you go.")
    print("you come up to a dead end, although you feel around and find a ledge that you can fit through.")
    print("take a large breath to slim your body and rip your body through the crunching ledge.")
    print("you struggle to crawl througth the ledge, but you are making progress.")
    print("what do you do?")
    print("1. keep going")
    print("2. turn back")
    rusticpath3 = input(">>>")
            
    if rusticpath3 == "1":
                endless_cave()
            
    elif rusticpath3 == "2":
                bad_cave_ending()
            
    else:
                print("invalid input, try again.")
                into_the_cave()

def stream():
    print("you follow the stream, the water is cold and refreshing.")
    print("you see a small cabin in the distance.")
    print("what should you do?")
    print("1. approach the cabin")
    print("2. keep following the stream")
    print("3. turn back")

def opening():
    print("you walk throught the opening and find yourself in a strong meadow full of flowers and insects buzzing around.")
    print("its relaxing and you start to feel at peace.")
    print("what should you do?")
    print("1. lay down and relax")
    print("2. explore the meadow")
    print("3. turn back")

start_adventure()