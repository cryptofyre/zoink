# Starting application.
print("Would you like to play Zoink?")
playing = input("Type 1 to play type 2 to quit ")
print("Note: All actions that involve fighting or running require secondary confirmation and use punctuation and capitalization if their are any.")
time.sleep(2)
print("Starting game!")
time.sleep(3)
# Grabbing User Info
if playing == "1" :
  print("Starting Zoink!")
  os.system("clear")
  print("Lets get your name.")
  username = input("Please state your name: ")
  os.system("clear")
  print ("Hello", username,"!")
  os.system("clear")
  print("Alright " + username + " lets get going!")
  time.sleep(1)
  os.system("clear")
# Game started
  print("Your name is Shaggy and you are currently at a Nordstrom in Kurkuk, Iraq. ")
  print("Please input your movement. You can move North and West.")
  loc1 = input("")
  if loc1 == ("go north"):
    os.system("clear")
    print("You walk north attempting to avoid the makeup artists but you are stopped by a YouTuber named James Charles. He asks if you would be intrested in a video with him. What do you say? (y for yes n for no)")
    if input()==("y"):
      os.system("clear")
      print("James walks towards you while holding a makeup brush. With one click you become the big gay. You Died from Gayness")
    elif input()==("n"):
      os.system("clear")
      print("Then perish you non homophobic scum!" " James goes to swing at you. Shall I throw a punch or run (p for punch or r for run?")
      if input()==("p"):
        os.system("clear")
        print("You attempt to throw a punch but a mall guard draws his gun before you could punch him and he shoots you.")
        time.sleep(10)
        os.system("clear")
        print("You have died")
# Secondary method of saying "north"
  elif loc1 == ("North"):
      os.system("clear")
      print("You walk north attempting to avoid the makeup artists but you are stopped by a YouTuber named James Charles. He asks if you would be intrested in a video with him. What do you say? (y for yes n for no)")
      if input()==("y"):
        print(" James walks towards you while holding a makeup brush. With one tap you become ill. Then you realize the big gay has taken over your soul. ")
        time.sleep(2)
        os.system("clear")
        print("You died. (a quite a odd way I must add.) [Ending 1]")
      elif input()==("n"):
        os.system("clear")
        print("Then perish you non homophobic scum!" " James goes to swing at you. Shall I throw a punch or run (p for punch or r for run?")
        if input()==("p"):
          os.system("clear")
          print("You attempt to throw a punch but a mall guard draws his gun before you could punch him and he shoots you.")
          os.system("clear")
          print("You have died [Ending 2]")
        elif input()==("r"):
          os.system("clear")
          print("You run as fast as you can all you hear behind you is gun shots you turn to see him lying lifeless on the mall tile.")
          time.sleep(10)
          os.system("clear")
          print("After running for what seems like forever you are outside a McDonalds.")
          print("Enter the McDonalds? (y) (n)")
          loc2 = input()
          if loc2 == ("y"):
            print("You walk into the McDonalds and the employee at the order desk says 'Welcome to McDonalds! What would you like today!' [Big Mac] or [Whopper]")
            if input() == ("Big Mac"):
              print("The cashier gives you the burger and you proceed to walk out the door but it was a chungus Big Mac you are now extra thicc but the downside is your extra slow (Tip: Now attacking and running should only be used if it needs be try to avoid confrontation) ")
              print("You walk out side and see a shadow like figure walk towards you, he's holding something in his hand. Do you hide left, hide right, or fight.")
              if input()==("hide left"):
                print("The figure walks around the corner and sees you. He then pops a cap in your ass. The figure then notices your phone and calls your parents and siblings to tell them you are taken under hostage. Later the siblings and parents arrive and get shot in a quick and easy move.")
              time.sleep(5)
              os.system("clear")
              print("Worst Ending")
              if input()==("hide right"):
                print("He walks past you. You get away but you hear gunshots. The shadow figure shot up the McDonalds. ")
              time.sleep(5)
              os.system("clear")
              print("Good Ending")
              if input()==("fight"):
                print("You attempt to throw a punch but end up on the ground. In one swift move the shadow figure pops a cap in your ass but the extra thicc cheeks fire the bullet back towards the attacker killing him instantly.")
                time.sleep(5)
              os.system("clear")
              print("Best Ending")
        
            elif input()==("Whopper"):
              print("the cashier eyes turn red, blood stars raining like a waterfall. The cashier yells words that cant be comprehended.") 
              print ("Ronald McDonald him self yells at you ""What did you just say!" )
              print("You got three options a. leave. b. say Big Mac. c. die")
            if input()==("a"):
              print("you walk away and the doors then turn into a brick wall he then proceeds to stab you with his extral large fry.")
              time.sleep(5)
              os.system("clear")
              print(" you died to a fucking clown, and the world biggets fry. What a tasty way to die. [Ending 3]")
            elif input()==("b"):
              print("You try to speak but your so terrifed that you just piss your self. Ronald yells speak You whimper and say Big Mac.")
              print(" Ronlad knows you were lying so he gives you a Big Mac with rat poison. You have the urge to puke, so you go to th bathroom and insted of puking food out you puke your entire intestinal track out.")
              time.sleep(2)
              os.system("clear")
              print("Jessus Christ! [Ending 4]")
            elif input("c"):
              print("You pull out your dick and start swingin it towards Ronald to spare you some time.")
              time.sleep(2)
              os.system("clear")
              print(" oh shit you traded.[Ending 5]")
            elif loc2 == ("n"):
              print("your out side and see a shadowy figure walk towards you, he's holding somthing in his hand. do you hide left, hide right, or fight.")
            if input()==("hide left"):
              print("The figure walks around the corner and sees you. He then caps your ass.")
              time.sleep(2)
              os.system("clear")
              print("[Ending 8]")
            if input()==("hide right"):
                print("He walks past you. You get away but you hear gunshots. Mr King shot up the mcdonalds. ")
                time.sleep(2)
                os.system("clear")
                print("Good Ending 1-2 ending of north route.")
            if input()==("fight"):
              print("You punched Mr.King in the face so he shoots you. ")
              time.sleep(2)
              os.system("clear")
              print("[ending 9]")
