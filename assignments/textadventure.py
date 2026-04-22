# setting-
# time: mid day like 3:00pm
# place: forest - warm summer day.
# mood: lost
key = False
forest_medow = False

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

def stream():
    print("you follow the stream, the water is cold and refreshing.")
    print("you see a small cabin in the distance.")
    stream_1()

def stream_1():
    print("what should you do?")
    print("1. approach the cabin")
    print("2. keep following the stream")
    print("3. turn back")
    stream1 = input(">>>")

    if stream1 == "1":
         stream_cabin()

def stream_cabin():
     print("you approach the still dark cabin surrounded by dense mahogany trees, its rustic boards are weathered and worn.")
     print("you question whether this is the best idea, but you decide to continue forward.")
     print("you place your hand on the frigid brass handle and turn it, the door creaks open.")
     print("you look inside and see a naturaly lit living room with wooden floors, a fireplace and a small kitchen.")
     print("you look further into the house and see a staircase leading to a second floor.")
     print("what do you do?")
     stream_cabin_1()

def stream_cabin_1():
     print("1. explore the living room")
     print("2. explore the kitchen")
     print("3. go up the stairs")
     stream_cabin1 = input(">>>")     

     if stream_cabin1 == "1":
          stream_cabin_livingroom()

     elif stream_cabin1 == "2":
          stream_cabin_kitchen()

     elif stream_cabin1 == "3":
          stream_cabin_stairs()
    
     else:
          print("invalid input, try again.")
          stream_cabin_1()


def stream_cabin_livingroom():
     print("you step into the living room, you asses the room and see a fireplace, some furniture, and a small table.")
     print("what will you explore first?")
     livingroom_1()



def livingroom_1():
        print("1. explore the fireplace")
        print("2. examine the table")
        print("3. sit on the couch")
        print("4. go back to the main area of the cabin")
        livingroom1 = input(">>>")

        if livingroom1 == "1":
            print("you walk over to the fireplace, there is no fire.")
            print("although, you see a small glimmer of light coming from under the burnt up charcoal.")
            print("you reach into the void black coals and pull out a small key.")
            print("you tell yourself that this key might be useful.")
            global key
            key = True
            livingroom_1()

        elif livingroom1 == "2":
            print("you approach the table and see the note.")
            print("the note reads: 'honey, I put the key in the ...' the rest of the note is illegible.")
            print("you place the note back on the table and continue to explore.")
            livingroom_1()

        elif livingroom1 == "3":
            print("you sit on the couch and feel comfortable.")
            livingroom_1()

        elif livingroom1 == "4":
            print("you decide to go back to the main area of the cabin.")
            stream_cabin_1()

        else:
            print("invalid input, try again.")
            livingroom_1()

def stream_cabin_kitchen():
     print("you walk into the kitchen, you are blinded by the light coming from the window.")
     print("your eyes adjust and you see a small counter with a sink and a stove.")
     print("what will you explore first?")
     kitchen()

def kitchen():
        print("1. explore the sink")
        print("2. explore the stove")
        print("3. go back to the main area of the cabin")
        kitchen1 = input(">>>")
    
        if kitchen1 == "1":
            print("you walk over to the crusted sink, there is nothing but a few dirty dishes.")
            kitchen()
    
        elif kitchen1 == "2":
            print("you open the oven and see that it is empty.")
            kitchen()

        elif kitchen1 == "3":
            print("you decide to go back to the main area of the cabin.")
            stream_cabin_1()
    
        else:
            print("invalid input, try again.")
            kitchen()

def stream_cabin_stairs():
    print("you make your way to the stairs, there is minimal light coming from the second floor.")
    print("you take your first step and hear a loud creak, the tension in the air is choking you.")
    print("you make your way up the stairs, you see a small hallway with 2 doors and a window at the end of the hall.")
    print("what do you do?")
    stairs()

def stairs():
    print("1. open the first door")
    print("2. open the second door")
    print("3. look out the window")
    print("4. go back down the stairs")
    stairs1 = input(">>>")
    
    if stairs1 == "1":
         print("you try to twist the doorknob but its locked.")
         global key
         if key == True:
              print("you remember you have the key, you place it in the lock and turn it, the door creaks open.")
              door1()

         else:
            print("you notice the door has a lock.")
            stairs()
        
    elif stairs1 == "2":
         print("you open the second door and see a small bedroom with a bed, a dresser and a nightstand.")
         print("what do you explore first?")
         bedroom2()
    
    elif stairs1 == "3":
         print("you look out the window and see the dense forest all around you, you see a small stream flowing and a path leading to an opening in the forest.")
         global forest_medow
         forest_medow = True
         print("you return to the end of the hallway.")
         stairs()

def door1():
    print("placeholder door 1.")
      

def bedroom2():
    print("placeholder door 2.")








def opening():
    print("you walk throught the opening and find yourself in a strong meadow full of flowers and insects buzzing around.")
    print("its relaxing and you start to feel at peace.")
    print("what should you do?")
    print("1. lay down and relax")
    print("2. explore the meadow")
    print("3. turn back")

start_adventure()