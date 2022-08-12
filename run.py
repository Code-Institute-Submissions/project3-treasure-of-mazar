import random
import time
import sys
import os


class PlayerAttributes:
    def __init__(self, name, location, dagger):
        self.name = name
        self.location = location
        self.dagger = dagger


player = PlayerAttributes('', '', False)


class StatueWeapons:
    def __init__(self, weapons):
        self.weapons = weapons


statue_weapons = StatueWeapons('')


def introduction():
    """
    Opens the game with the title screen and introduction
    to the story of the game.
    """
    os.system('cls||clear')
    print()
    print("""
 _____                                          __  ___  ___                    
|_   _|                                        / _| |  \/  |                    
  | |_ __ ___  __ _ ___ _   _ _ __ ___    ___ | |_  | .  . | __ _ ______ _ _ __ 
  | | '__/ _ \/ _` / __| | | | '__/ _ \  / _ \|  _| | |\/| |/ _` |_  / _` | '__|
  | | | |  __/ (_| \__ \ |_| | | |  __/ | (_) | |   | |  | | (_| |/ / (_| | |   
  \_/_|  \___|\__,_|___/\__,_|_|  \___|  \___/|_|   \_|  |_/\__,_/___\__,_|_|   
    """)
    print()
    print("""
     
     ]╢▒▒▒▒▒▒╣▒▒▒▒▒▒▒▒▒╣▒▒▒▒▒╣▒▒▒╢╫╣╬▓▓▀▀╣
     ╘▒▒▒▒▒▒▒▒▒░░░░░░░ ░░░░▒▒▒▒▒▒▒▒▒▒░▒▒▒╢
      ▒▒░▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒░▒
      ╙▒░░▒▒▒▒▒▒▒╣▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░
       ╚▒▒▒▒▒▒╣╣╣╣╣╣▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░╫╣▒▒`
        "╬▒░░▒╢╣╣╣╣╣▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢╫╣▒▒
           ▀╩▓╣╢▓▓▓▓▓▓▓▓▓▓╣╣╢╣╣╣╣▒▓▀╙
                 `"╙▓▓▓╣╣▓▓▓"``
                    ╟▓▓▓▓▓▓⌐
                     ╟╢▓▓▓M
                     ▐▓▓▌▓
                   ,╔╣▓╬▀▀▀╖,
                 ╫▓▒╢╣╬@▒░╬╬╣▓Γ
    """)
    print()
    print("Long ago, a powerful king named Mazar reigned undisputed.\n")
    print("Until one day, he was betrayed by his son and his reign ended.\n")
    print("Before his death, Mazar built a great tomb and stashed his most prized treasure.\n")
    print("It's wherabouts laid secret for untold years...\n")
    print("Until suddenly, rumours began to spread of its supposed location.\n")
    print("Many went in search for the great treasures within.\n")
    print("But not a single soul has returned to tell the tale.\n")
    print("Will you enter the tomb and succeed where others have failed...?\n")
    print("Do you have what it takes to claim the fabled Treasure of Mazar?\n")
    start_game()


def start_game():
    """
    Lets the user choose to start the game and enter
    their name before beginning. Sets the player values
    to default.
    """
    player.dagger = False
    weapon_combos = ['Sword and Axe', 'Bow and Sword', 'Bow and Axe']
    statue_weapons.weapons = random.choice(weapon_combos)
    
    start_choice = input("Are you ready to start your adventure? (Yes/No)\n")
    if start_choice.lower().strip() == "yes":
        player.name = input("What is your name?\n")
        print(f"Welcome {player.name}. Your adventure awaits!\n")
        begin_adventure()
    elif start_choice.lower().strip() == "no":
        print("Very well... Please take your time.")
        time.sleep(5)
        introduction()
    else:
        print("Please type Yes or No!")
        start_game()


def begin_adventure():
    """
    Sets the beginning of the story and provides the choice
    between entering the tomb or not.
    """
    print()
    print("Hearing the rumours of the tomb of Mazar, you set off in search of fortune.\n")
    print("You arrive at a misty ruin in a forest where the air is still.\n")
    print("Shivers run down your spine as you see a great doorway to a tomb.\n")
    print(f"{player.name}: 'This must be it... The tomb of Mazar!'\n")
    print(f"{player.name}: 'Somewhere inside is the fabled Treasure of Mazar...'\n")
    print(f"{player.name}: 'If I find that, I could live like a king!'\n")
    print(f"{player.name}: 'But then again, nobody has ever come out alive...'\n")
    print(f"{player.name}: 'Should I really risk my life for this?'\n")
    enter_choice = input("Do you want to enter the tomb? (Yes/No)\n")
    if enter_choice.lower().strip() == "yes":
        print(f"{player.name}: 'There's no turning back now! Here I go!'\n")
        print("You push open the great tomb doors and make your way into the depths below.\n")
        enter_tomb()
    elif enter_choice.lower().strip() == "no":
        print(f"{player.name}: 'No... I can't do this. My life is more valuable than any treasure.'\n")
        end_1()
    else:
        print("Please type Yes or No!")
        time.sleep(2)
        begin_adventure()


def enter_tomb():
    """
    Displays the story if the player enters the tomb
    and sets the player location to Tomb. Runs the path_choice
    function.
    """
    player.location = "Tomb"

    print()
    print("As you enter the great tomb, a sense of dread washes over you.\n")
    print("You notice piles of bones litter the room around you.\n")
    print("The path ahead is dark and only lit by the light outside.\n")
    print("You pull out your torch as you continue forward.\n")
    print(f"{player.name}: 'Here I go... Into the dark unknown...'\n")
    print("You walk the dimly lit passage, your footsteps echoing.\n")
    print("Suddenly, you come to a fork in the road!\n")
    print("To the left appears to be a dim room with a large door.\n")
    print("To the right, you see a dark room filled with pots.\n")
    print(f"{player.name}: 'Hmm... Which path should I take?'\n")
    path_choice()


def path_choice():
    """
    Gives the player a choice between paths and runs the
    function for the correct path depending on input and player
    location.
    """
    path = input("Which path do you take? (Left/Right)\n")
    if path.lower().strip() == "left":
        if player.location == "Tomb":
            path_1()
        elif player.location == "Path 2":
            path_4()
    elif path.lower().strip() == "right":
        if player.location == "Tomb":
            path_2()
        elif player.location == "Path 2":
            path_5()
    else:
        print("Please enter either Left or Right!")
        path_choice()
        

def path_1():
    """
    Displays the story for and decisions for path 1. Sets
    the player location to path 1.
    """
    player.location = "Path 1"

    print()
    print("You enter the dim room with an imposing, large door\n")
    print("The door appears to be made of stone, and has two large handles.\n")
    print("Above the door sits a ghastly stone face staring down at you.\n")
    print(f"{player.name}: 'Creepy... It looks like it's judging me.'\n")
    print(f"{player.name}: 'Should I try to open the door or go back the other way?'\n")
    door_choice = input("Open the door? (Yes/No)\n")
    if door_choice.lower().strip() == "yes":
        print(f"{player.name}: 'What's the worst that can happen?'\n")
        print("You try to pull on the door handles...\n")
        print("The handles are cold and heavy and the door refuses to budge.\n")
        print("Suddenly a loud voice booms through the room!\n")
        print("'FOOLISH MORTAL! Who dares disturb this tomb?'\n")
        print("In a panic, you look around the room, wondering where the voice came from.\n")
        print("You see the statue above the door staring at you with red eyes!\n")
        print(f"{player.name}: 'Um, my name is {player.name}!'\n")
        print(f"'Very well, {player.name.upper()}! Answer my riddle and you may pass.'\n")
        print("'But fail, and you will be reduced to ash where you stand!'\n")
        print("You try to move, but you seem to be frozen in place!\n")
        print(f"{player.name}: I guess I have no choice...\n")
        print(f"{player.name}: 'What is your riddle?'\n")
        print("'Answer me this:'\n")
    if door_choice.lower().strip() == "no":
        print(f"{player.name}: 'I think I preferred the other room...'\n")
        print("You decide to turn around and head back to the room with pots.\n")
        time.sleep(2)
        path_2()
    else:
        print("Please type Yes or No!")
        time.sleep(2)
        path_1()


def path_2():
    """
    Displays the story and decisions for path 2. Sets
    the player location to path 2.
    """
    player.location = "Path 2"

    print()
    print("You enter a dark room filled with strange stone pots.\n")
    print(f"{player.name}: 'What's up with these pots? I can't see inside them.'\n")
    print("Inspecting the pots with your torch, they appear pitch black inside.\n")
    print("Every pot in the room seems to be the exact same.\n")
    pot_choice()
    print("Continuing into the tomb, you come to another crossroad!\n")
    print("To the left, you hear a strange noise, almost like a deep snore.\n")
    print("To the right, you notice an orange glow and an intense wave of heat.\n")
    path_choice()


def path_3():
    """
    Displays the story and decisions for path 3. Sets
    the player location to path 3.
    """


def path_4():
    """
    Displays the story and decisions for path 4. Sets
    the player location to path 4.
    """
    print()
    player.location = "Path 4"
    print("You enter a small room covered in a strange substance.\n")
    print("A foul smell burns your nostrils as you try not to gag.\n")
    print(f"{player.name}: 'Eugh! What is that disgusting smell!?'\n")
    print(f"{player.name}: 'And this substance is so sticky! It's hard to move!'\n")
    print("As you make your way through the room, the strange noise gets louder.\n")
    print("Soon, you come face to face with a large troll slumpt over in a doorway.\n")
    print(f"{player.name}: 'He seems to be sleeping... He snores like my grandmother!'\n")
    print("It appears the troll blocks the only path forward.\n")
    print("You may be able to sneak around, but you may risk waking him up.\n")
    print("There is a large rock on the floor next to the troll.\n")
    if player.dagger:
        print("Maybe that black dagger could be of use?\n")
    print(f"{player.name}: 'What should I do?\n")
    print("1. Attempt to sneak around the troll.\n")
    print("2. Try to kill the troll with the large rock.\n")
    if player.dagger:
        print("3. Use the black dagger to kill the troll.\n")
    troll_choice()



def path_5():
    """
    Displays the story and decisions for path 5. Sets
    the player location to path 5.
    """


def path_6():
    """
    Displays the story and decisions for path 6. Sets
    the player location to path 6.
    """


def pot_choice():
    """
    Asks the user for their input on whether they wish
    to search the pots in path 2 and displays an output
    depending on their choice.
    """
    choice = input("Do you wish to put your hand in and search the pots? (Yes/No)\n")
    if choice.lower().strip() == "yes":
        print("You put your hand into the pot...\n")
        print("It feels like your hand was somehow detached from your body.\n")
        print("Suddenly, you feel an odd, cold object!\n")
        print("You begin to pull...\n")
        print("And a pitch black dagger comes out!\n")
        print(f"{player.name}: 'Whoa! It seems to absorb all the light around it...'\n")
        print("You put the dagger in your bag.\n")
        player.dagger = True
    elif choice.lower().strip() == "no":
        print(f"{player.name}: 'I have a bad feeling about putting my hand in those pots.'\n")
        print("You decide not to search the pots and carry on to the next room.\n")
    else:
        print("Please type Yes or No!")
        pot_choice()


def troll_choice():
    """
    Asks the user for their input on what they wish
    to do with the troll in path 4 and displays an
    output depending on their choice.
    """
    if player.dagger:
        choice = input("Choose an option: (1/2/3)\n")
    else:
        choice = input("Choose an option: (1/2)\n")
    if choice.strip() == "1":
        print("You try to sneak around the troll.\n")
        print("As you get close, the troll begins to grumble...\n")
        sneak_chance = random.randrange(1,5)
        if sneak_chance > 3:
            print("You successfully sneak past the troll!\n")
            print(f"{player.name}: 'Phew! that was close!'\n")
            print("You continue on through the tomb.\n")
            statue_room()
        elif sneak_chance <= 3:
            print("You fail to sneak past the troll and it wakes up!\n")
            print("The troll grabs you and begins to eat you!\n")
            death()
    elif choice.strip() == "2":
        print("You attempt to pick up the large rock.\n")
        print("It's heavy but you manage to pick it up.\n")
        print("You lift the rock above your head and bring it down on the troll!\n")
        print(f"{player.name}: 'Hiyah!'\n")
        print("The rock bounces off the troll without a scratch.\n")
        print("Suddenly, the troll wakes up!\n")
        print(f"{player.name}: 'Uh oh!'\n")
        print("The troll pummels you with his fist, leaving a bloody mess!\n")
        death()
    elif choice.strip() == "3" and player.dagger:
        print("You take out the pitch black dagger...\n")
        print("You plunge the dagger into the skull of the troll!\n")
        print("The troll lets out a blood curdling cry before falling silent.\n")
        print(f"{player.name}: 'Wow! I can't believe I did it!'\n")
        print("The black dagger shatters and is now useless.\n")
        print("You walk around the dead troll and continue on.\n")
        statue_room()
    else:
        if player.dagger:
            print("Please type 1, 2 or 3!")
            troll_choice()
        else:
            print("Please type 1 or 2!")
            troll_choice()


def statue_room():
    """
    Displays the story and decisions for the statue room.
    """
    print()
    print("You enter a room with 3 large imposing statues.\n")
    print("Two of the statues are holding weapons but one is not.\n")
    print("There is a table in front of you with 3 stone weapons on it.\n")
    print("They appear to be an axe, a sword and a bow.\n")
    print(f"{player.name}: 'What if I place a weapon on the odd statue?'\n")
    statue_choice()
    print("A rumbling can be heard...\n")
    print("The doorway ahead opens!\n")
    print("You head through to the next area.\n")


def statue_choice():
    """
    Displays the random weapon combo for the statues.

    """
    print(f"{player.name}: 'The two statues with weapons are holding a {statue_weapons.weapons}.'\n")
    print(f"{player.name}: 'What should I take from the table?'\n")
    weapon_choice = input("Axe, Sword or Bow?\n")
    if weapon_choice.lower().strip() == "axe" and statue_weapons.weapons == "Bow and Sword":
        print("You take the Axe and put it on the statue...\n")
    elif weapon_choice.lower().strip() == "sword" and statue_weapons.weapons == "Bow and Axe":
        print("You take the Sword and put it on the statue...\n")
    elif weapon_choice.lower().strip() == "bow" and statue_weapons.weapons == "Sword and Axe":
        print("You take the Bow and put it on the statue...\n")
    else:
        if weapon_choice.lower().strip() == "axe" or weapon_choice.lower().strip() == "bow" or weapon_choice.lower().strip() == "sword":
            print(f"You take the {weapon_choice} and put it on the statue...\n")
            print("Nothing seems to happen...\n")
            print("Suddenly, the statues come to life!\n")
            print(f"{player.name}: 'Oh no! I messed up!'\n")
            print("The statues get closer and you try to run...\n")
            print("You trip over on a piece of rock!\n")
            print("Everything fades to black as the sound of stone footsteps get closer...\n")
            death()
        print("Please enter Axe, Sword or Bow!")
        statue_choice()


def try_again():
    """
    Asks the user if they wish to play again and takes
    their input. Runs the introduction again if they
    choose yes, and ends the game if they choose no.
    """
    play_again = input("Do you wish to play again? (Yes/No)\n")
    if play_again.lower().strip() == "yes":
        introduction()
    elif play_again.lower().strip() == "no":
        print("Thank you for playing!")
        sys.exit()
    else:
        print("Please type Yes or No!")
        try_again()


def death():
    """
    Displays the death message.
    """
    print()
    print("""

▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄  ▐██▌ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌ ▐██▌ 
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌ ▐██▌ 
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌ ▓██▒ 
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓  ▒▄▄  
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒  ░▀▀▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒  ░  ░ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░     ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░     ░    
 ░ ░                           ░                  ░            
    """)
    print("Better luck next time!\n")
    try_again()


def end_1():
    """
    Displays ending 1.
    """
    print()
    print("You decide to turn back and live another day.\n")
    print("The treasure was tempting, but it wasn't worth risking your life.\n")
    print("You make your way back home to your family and friends.\n")
    print("And think about what the future has in store for you...\n")
    print("------ENDING 1------\n")
    try_again()


def end_2():
    """
    Displays ending 2.
    """


def end_3():
    """
    Displays ending 3.
    """


def end_4():
    """
    Displays ending 4.
    """



introduction()