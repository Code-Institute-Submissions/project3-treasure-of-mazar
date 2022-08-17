"""
File to run the game.
"""
import random
import time
import sys
import os
import colorama
from colorama import Fore, Style
import ascii_art

colorama.init()


# Constants for time.sleep to run a delay in seconds.
A = 1
B = 2
C = 5
D = 0.3
E = 0.5


class PlayerAttributes:
    """
    Stores attributes for the player such as name,
    location and items.
    """
    def __init__(self, name, location, dagger, key, blessing, secret):
        self.name = name
        self.location = location
        self.dagger = dagger
        self.key = key
        self.blessing = blessing
        self.secret = secret


player = PlayerAttributes('', '', False, False, False, False)


class Random:
    """
    Stores random weapon combo data for the statues
    room and random riddle for path 1.
    """
    def __init__(self, weapons, riddle):
        self.weapons = weapons
        self.riddle = riddle


random_select = Random('', '')


def typing(text):
    """
    Prints text slowly in a typewriter style.
    """
    # Used from tutorial on 101computing.net
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


def introduction():
    """
    Opens the game with the title screen and introduction
    to the story of the game.
    """
    os.system('cls||clear')
    print()
    print(ascii_art.TITLE)
    print()
    print(Fore.YELLOW + ascii_art.CHALICE)
    print(Fore.RESET)
    print()
    time.sleep(D)
    typing("Long ago, a powerful king named Mazar reigned undisputed.\n\n")
    typing("Until one day, he was betrayed by his son, ending his reign.\n\n")
    typing("Before his death, Mazar built a great tomb and stashed his most\n"
           "prized treasure.\n\n")
    typing("It's wherabouts laid secret for untold years...\n\n")
    typing("Until suddenly, rumours began to spread of its supposed "
           "location.\n\n")
    typing("Many went in search for the great treasures within.\n\n")
    typing("But not a single soul has returned to tell the tale.\n\n")
    typing("Will you enter the tomb and succeed where others have "
           "failed...?\n\n")
    typing("Do you have what it takes to claim the fabled Treasure of "
           "Mazar?\n\n")

    start_game()


def start_game():
    """
    Lets the user choose to start the game and enter
    their name before beginning. Sets the player values
    to default. Sets a random weapon combo for the statue
    room.
    Asks the user if they wish to view the instructions.
    """
    player.dagger = False
    player.key = False
    player.blessing = False
    player.secret = False
    weapon_combos = ['Sword and Axe', 'Bow and Sword', 'Bow and Axe']
    random_select.weapons = random.choice(weapon_combos)

    instructions_choice = input("Do you wish to view the instructions? "
                                "(Yes/No)\n")

    if instructions_choice.lower().strip() == "yes":
        print()
        typing("Your goal is to enter the tomb and claim the Treasure of "
               "Mazar.\n")
        typing("You will have multiple paths to choose from during your "
               "journey.\n")
        typing("During your journey you may encounter challenges that you must"
               " overcome.\n")
        typing("Different paths will lead to different encounters.\n")
        typing("Some encounters may provide you with useful items.\n")
        typing("Use these to help you progress through the tomb.\n")
        typing("Victory is never guaranteed, and you may need to get lucky.\n")
        typing("Try to find all the endings, and good luck!\n\n")
        time.sleep(B)
    elif instructions_choice.lower().strip() == "no":
        print("Okay! Good luck!\n")
    else:
        print("Please type Yes or No!")
        start_game()

    start_choice = input("Are you ready to start your adventure? (Yes/No)\n")

    while True:
        if start_choice.lower().strip() == "yes":
            player.name = input("What is your name?\n")
            while True:
                if (len(player.name.strip()) > 0 and
                        len(player.name.strip()) <= 30):
                    typing(f"Welcome {player.name}. Your adventure awaits!"
                           "\n\n")
                    begin_adventure()
                    break
                else:
                    print("Name must be more than 0 characters and no more "
                          "than 30!\n")
                    player.name = input("Please type a different name!\n")
        elif start_choice.lower().strip() == "no":
            typing("Very well... Please take your time.")
            time.sleep(C)
            introduction()
            break
        else:
            start_choice = input("Please type Yes or No!")
    return


def begin_adventure():
    """
    Sets the beginning of the story and provides the choice
    between entering the tomb or not.
    """
    print()
    typing("Hearing the rumours of the tomb of Mazar, you set off in search "
           "of fortune.\n\n")
    typing("You arrive at a misty ruin in a forest where the air is still."
           "\n\n")
    typing("Shivers run down your spine as you see a great doorway to a "
           "tomb.\n\n")
    typing(f"{player.name}: 'This must be it... The tomb of Mazar!'\n\n")
    typing(f"{player.name}: 'Somewhere inside is the fabled Treasure of "
           "Mazar!'\n\n")
    typing(f"{player.name}: 'If I find that, I could live like a king!'\n\n")
    typing(f"{player.name}: 'But then again, nobody has ever come out "
           "alive.'\n\n")
    typing(f"{player.name}: 'Should I really risk my life for this?'\n\n")
    enter_choice = input("Do you want to enter the tomb? (Yes/No)\n")

    while True:
        if enter_choice.lower().strip() == "yes":
            typing(f"{player.name}: 'There's no turning back now! Here I go!'"
                   "\n\n")
            typing("You push open the great tomb doors and make your way into "
                   "the depths below.\n\n")
            enter_tomb()
            break
        elif enter_choice.lower().strip() == "no":
            typing(f"{player.name}: 'No... I can't do this. My life is more\n"
                   "valuable than any treasure.'\n\n")
            end_1()
            break
        else:
            enter_choice = input("Please type Yes or No!\n")
    return


def enter_tomb():
    """
    Displays the story if the player enters the tomb
    and sets the player location to Tomb. Runs the path_choice
    function.
    """
    player.location = "Tomb"

    print()
    typing("As you enter the great tomb, a sense of dread washes over you."
           "\n\n")
    typing("You notice piles of bones litter the room around you.\n\n")
    typing("The path ahead is dark and only lit by the light outside.\n\n")
    typing("You pull out your torch as you continue forward.\n\n")
    typing(f"{player.name}: 'Here I go... Into the dark unknown...'\n\n")
    typing("You walk the dimly lit passage, your footsteps echoing.\n\n")
    typing("Suddenly, you come to a fork in the road!\n\n")
    typing("To the left appears to be a dim room with a large door.\n\n")
    typing("To the right, you see a dark room filled with pots.\n\n")
    typing(f"{player.name}: 'Hmm... Which path should I take?'\n\n")
    path_choice()
    return


def path_choice():
    """
    Gives the player a choice between paths and runs the
    function for the correct path depending on input and player
    location.
    """
    time.sleep(A)
    path = input("Which path do you take? (Left/Right)\n")
    if path.lower().strip() == "left":
        if player.location == "Tomb":
            path_1()
        elif player.location == "Path 1":
            path_5()
        elif player.location == "Path 2":
            path_4()
    elif path.lower().strip() == "right":
        if player.location == "Tomb":
            path_2()
        elif player.location == "Path 1":
            path_3()
        elif player.location == "Path 2":
            path_5()
    else:
        print("Please enter either Left or Right!")
        path_choice()
    return


def path_1():
    """
    Displays the story for and decisions for path 1. Sets
    the player location to path 1. Sets the player blessing to
    True if they answer the riddle correct.
    """
    player.location = "Path 1"

    print()
    typing("You enter the dim room with an imposing, large door\n\n")
    typing("The door appears to be made of stone, and has two large handles."
           "\n\n")
    typing("Above the door sits a ghastly stone face staring down at you.\n\n")
    typing(f"{player.name}: 'Creepy... It looks like it's judging me.'\n\n")
    typing(f"{player.name}: 'Should I try to open the door or go back the \n"
           "other way?'\n\n")
    door_choice()
    riddle_choice()
    print(Fore.RED + Style.BRIGHT)
    typing("'Impressive, mortal... You are wise indeed!'\n\n")
    typing("'Take my blessing and venture forth! Your treasure lies deeper.'"
           "\n")
    print(Style.RESET_ALL)
    player.blessing = True
    typing(f"{player.name}: 'Um, thank you. Talking... Stone face?'\n\n")
    typing("The great door opens before you and you carefully go through.\n\n")
    typing("As you travel onward, you come to another crossroad!\n\n")
    typing("To the left, you notice an orange glow and an intense wave of "
           "heat.\n\n")
    typing("To the right, you feel a cold chill and an ominious presence.\n\n")
    path_choice()
    return


def door_choice():
    """
    Asks the user for their input on whether they wish to
    open the door in path 1 and displays an output depending
    on their choice.
    """
    open_door = input("Open the door? (Yes/No)\n")

    if open_door.lower().strip() == "yes":
        typing(f"{player.name}: 'What's the worst that can happen?'\n\n")
        typing("You try to pull on the door handles...\n\n")
        typing("The handles are cold and heavy and the door refuses to "
               "budge.\n\n")
        typing("Suddenly a loud voice booms through the room!\n")
        print(Fore.RED + Style.BRIGHT)
        typing("'FOOLISH MORTAL! Who dares disturb this tomb?'\n")
        print(Style.RESET_ALL)
        typing("In a panic, you look around the room, wondering where the "
               "voice came from.\n\n")
        typing("You see the statue above the door staring at you with red "
               "eyes!\n\n")
        typing(f"{player.name}: 'Um, my name is {player.name}!'\n")
        print(Fore.RED + Style.BRIGHT)
        typing(f"'Very well, {player.name.upper()}! Answer my riddle and\n"
               "you may pass.'\n\n")
        typing("'But fail, and you will be reduced to ash where you stand!'"
               "\n")
        print(Style.RESET_ALL)
        typing("You try to move, but you seem to be frozen in place!\n\n")
        typing(f"{player.name}: 'I guess I have no choice...'\n\n")
        typing(f"{player.name}: 'What is your riddle?'\n")
        print(Fore.RED + Style.BRIGHT)
        typing("'Answer me this:'\n")
        print(Style.RESET_ALL)
    elif open_door.lower().strip() == "no":
        typing(f"{player.name}: 'I think I preferred the other room...'\n\n")
        typing("You decide to turn around and head back to the room with "
               "pots.\n\n")
        path_2()
    else:
        print("Please type Yes or No!")
        door_choice()
    return


def path_2():
    """
    Displays the story and decisions for path 2. Sets
    the player location to path 2.
    """
    player.location = "Path 2"

    print()
    typing("You enter a dark room filled with strange stone pots.\n\n")
    typing(f"{player.name}: 'What's up with these pots?\n"
           "I can't see inside them.'\n\n")
    typing("Inspecting the pots with your torch, they appear pitch black "
           "inside.\n\n")
    typing("Every pot in the room seems to be the exact same.\n\n")
    pot_choice()
    typing("Continuing into the tomb, you come to another crossroad!\n\n")
    typing("To the left, you hear a strange noise, almost like a deep "
           "snore.\n\n")
    typing("To the right, you notice an orange glow and an intense wave of "
           "heat.\n\n")
    path_choice()
    return


def pot_choice():
    """
    Asks the user for their input on whether they wish
    to search the pots in path 2 and displays an output
    depending on their choice. Sets the dagger variable to
    True if the pots are searched.
    """
    choice = input("Put your hand in and search the pots? (Yes/No)\n")

    if choice.lower().strip() == "yes":
        typing("You put your hand into the pot...\n\n")
        typing("It feels like your hand was somehow detached from your body."
               "\n\n")
        typing("Suddenly, you feel an odd, cold object!\n\n")
        typing("You begin to pull...\n\n")
        time.sleep(A)
        typing("And a pitch black dagger comes out!\n\n")
        typing(f"{player.name}: 'Whoa! It seems to absorb all the light\n"
               "around it...'\n\n")
        typing("You put the dagger in your bag.\n\n")
        player.dagger = True
    elif choice.lower().strip() == "no":
        typing(f"{player.name}: 'I have a bad feeling about putting my hand\n"
               "in those pots.'\n\n")
        typing("You decide not to search the pots and carry on to the next "
               "room.\n\n")
    else:
        print("Please type Yes or No!")
        pot_choice()
    return


def path_3():
    """
    Displays the story and decisions for path 3.
    """
    print()
    typing("You enter a large dark room illuminated only by your torch.\n\n")
    typing("Cold air chills you to the bone and you feel uneasy.\n\n")
    typing(f"{player.name}: 'Brrr! It's freezing in here. Even my torch \n"
           "feels cold.'\n\n")
    typing("As you make your way through the room, you feel like you're "
           "being watched.\n\n")
    typing("Frost has formed on the floor making it hard to walk on.\n\n")
    typing("Out of the corner of your eye, you spot a ghostly figure.\n\n")
    typing("It watches you intently, almost as if it's beckoning you over."
           "\n\n")
    typing(f"{player.name}: 'Yikes, that's unsettling...'\n\n")
    ghost_choice()
    typing("You continue your adventure deeper into the tomb...\n\n")
    feast_room()
    return


def ghost_choice():
    """
    Asks the user for input on approaching the ghost.
    Displays an outcome depending on their choice.
    """
    approach_ghost = input("Approach the figure? (Yes/No)\n")

    if approach_ghost.lower().strip() == "yes":
        typing("You decide to approach the ominious figure...\n\n")
        typing(f"{player.name}: 'Hello? Can you hear me?'\n")
        print(Fore.MAGENTA + Style.BRIGHT)
        typing(f"???: '{player.name} why have you come?'\n")
        print(Style.RESET_ALL)
        typing("You feel a chill as the figure speaks.\n\n")
        typing(f"{player.name}: 'How do you know my name?'\n")
        print(Fore.MAGENTA + Style.BRIGHT)
        typing("???: 'I know the name of all who enter this tomb.'\n\n")
        typing(f"???: 'Now Answer me {player.name}: Why have you come?'\n")
        print(Style.RESET_ALL)
        typing("You're unsure how this figure may react to you coming for the "
               "treasure.\n\n")
        truth_choice()
    elif approach_ghost.lower().strip() == "no":
        typing(f"{player.name}: 'I'll pretend I didn't see that.\n\n")
        typing("You decide to continue your journey.\n\n")
        typing("As you walk on, you begin to get colder and colder...\n\n")
        typing("Your legs begin to seize in the freezing cold...\n\n")
        typing("And you fall to the ground, unable to breathe.\n\n")
        typing("You hear an ominious voice just before your senses fail.\n\n")
        print(Fore.MAGENTA + Style.BRIGHT)
        typing(f"???: 'You cannot escape fate {player.name}...'\n")
        print(Style.RESET_ALL)
        time.sleep(A)
        death()
    else:
        print("Please type Yes or No!")
        ghost_choice()
    return


def truth_choice():
    """
    Asks the user for input on telling the truth.
    Displays an outcome depending on their choice.
    """
    tell_truth = input(f"{player.name}: 'Should I tell it the truth?'\n"
                       "(Yes/No)\n")

    if tell_truth.lower().strip() == "yes":
        typing(f"{player.name}: 'I have come seeking the Treasure of Mazar.'"
               "\n\n")
        typing("The figure stares at you, making you feel more uneasy.\n")
        print(Fore.MAGENTA + Style.BRIGHT)
        typing(f"???: 'I sense truth in your words {player.name}.'\n\n")
        typing("???: 'After all, that is the reason for all who come here.'"
               "\n\n")
        typing("???: 'My name is Arlay, and I was once the architect of this "
               "tomb.'\n\n")
        typing("Arlay: 'But I was killed here after its completion.'\n\n")
        typing("Arlay: 'King Mazar betrayed me and cursed my soul to wander "
               "here.'\n\n")
        typing("Arlay: 'I have long awaited someone to make it this far.'\n\n")
        typing(f"Arlay: 'You, {player.name}, are the only one who has.'\n\n")
        typing("Arlay: 'Allow me to tell you the secret of this place.'\n\n")
        typing("Arlay: 'So that you may find what you seek and leave "
               "unharmed.'\n")
        print(Style.RESET_ALL)
        typing(f"{player.name}: 'Okay, but why help me?'\n")
        print(Fore.MAGENTA + Style.BRIGHT)
        typing("Arlay: 'So that I can have my revenge on King Mazar...'\n\n")
        typing("Arlay: 'Listen closely.'\n\n")
        typing("Arlay: 'When you take the treasure, the tomb is set to "
               "collapse.'\n\n")
        typing("Arlay: 'You can exit from where you came if you are lucky.'"
               "\n\n")
        typing("Arlay: 'But there is a secret exit in the treasure room.'\n\n")
        typing("Arlay: 'Go through the secret exit and you will be safe.'\n")
        print(Style.RESET_ALL)
        typing("You make a note of the secret exit.\n\n")
        player.secret = True
        typing(f"{player.name}: 'Thank you Arlay. I won't let you down!'\n\n")
    elif tell_truth.lower().strip() == "no":
        typing(f"{player.name}: 'I am just exploring!'\n\n")
        typing("The figure stares at you, and you feel a chill down your "
               "spine.\n")
        print(Fore.RED + Style.BRIGHT)
        typing("???: 'LIES!'\n")
        print(Style.RESET_ALL)
        typing("The figure lets out a piercing scream, causing your ears to "
               "ring.\n\n")
        typing("You start feeling nauseous as the room starts to spin.\n\n")
        typing("You collapse on the floor and hear a voice.\n\n")
        print(Fore.MAGENTA + Style.BRIGHT)
        typing(f"???: 'You are a fool {player.name}...\nLies do not get past "
               "me.'\n")
        print(Style.RESET_ALL)
        time.sleep(A)
        death()
    else:
        print("Please type Yes or No!")
        truth_choice()
    return


def path_4():
    """
    Displays the story and decisions for path 4. Checks if
    the player has picked up the dagger.
    """
    print()
    typing("You enter a small room covered in a strange substance.\n\n")
    typing("A foul smell burns your nostrils as you try not to gag.\n\n")
    typing(f"{player.name}: 'Eugh! What is that disgusting smell!?'\n\n")
    typing(f"{player.name}: 'And this substance is so sticky! It's hard to\n"
           "move!'\n\n")
    typing("As you make your way through the room, the strange noise gets "
           "louder.\n\n")
    typing("Soon, you come face to face with a large troll slumpt over in a "
           "doorway.\n\n")
    typing(f"{player.name}: 'He seems to be sleeping... He snores like my\n"
           "grandmother!'\n\n")
    typing("It appears the troll blocks the only path forward.\n\n")
    typing("You may be able to sneak around, but you may risk waking him up."
           "\n\n")
    typing("There is a large rock on the floor next to the troll.\n\n")
    if player.dagger:
        typing("Maybe that black dagger could be of use?\n\n")
    typing(f"{player.name}: 'What should I do?\n\n")
    typing("1. Attempt to sneak around the troll.\n")
    typing("2. Try to kill the troll with the large rock.\n")
    if player.dagger:
        typing("3. Use the black dagger to kill the troll.\n")
    troll_choice()
    return


def troll_choice():
    """
    Asks the user for their input on what they wish
    to do with the troll in path 4 and displays an
    output depending on their choice.
    If user enters 1, rolls a 1 in 4 chance of sneaking
    past the troll.
    """
    if player.dagger:
        choice = input("Choose an option: (1/2/3)\n")
    else:
        choice = input("Choose an option: (1/2)\n")

    if choice.strip() == "1":
        typing("You try to sneak around the troll.\n\n")
        typing("As you get close, the troll begins to grumble...\n\n")
        time.sleep(A)
        sneak_chance = random.randrange(1, 5)
        if sneak_chance > 3:
            typing("You successfully sneak past the troll!\n\n")
            typing(f"{player.name}: 'Phew! that was close!'\n\n")
            typing("You continue on through the tomb.\n\n")
            statue_room()
        elif sneak_chance <= 3:
            typing("You fail to sneak past the troll and it wakes up!\n\n")
            typing("The troll grabs you and begins to eat you!\n\n")
            death()
    elif choice.strip() == "2":
        typing("You attempt to pick up the large rock.\n\n")
        typing("It's heavy but you manage to pick it up.\n\n")
        typing("You lift the rock above your head and bring it down on the "
               "troll!\n\n")
        typing(f"{player.name}: 'Hiyah!'\n\n")
        typing("The rock bounces off the troll without a scratch.\n\n")
        typing("Suddenly, the troll wakes up!\n\n")
        typing(f"{player.name}: 'Uh oh!'\n\n")
        typing("The troll pummels you with his fist, leaving a bloody mess!"
               "\n\n")
        death()
    elif choice.strip() == "3" and player.dagger:
        typing("You take out the pitch black dagger...\n\n")
        typing("You plunge the dagger into the skull of the troll!\n\n")
        typing("The troll lets out a blood curdling cry before falling "
               "silent.\n\n")
        typing(f"{player.name}: 'Wow! I can't believe I did it!'\n\n")
        typing("The black dagger shatters and is now useless.\n\n")
        typing("You walk around the dead troll and continue on.\n\n")
        statue_room()
    else:
        if player.dagger:
            print("Please type 1, 2 or 3!")
            troll_choice()
        else:
            print("Please type 1 or 2!")
            troll_choice()
    return


def path_5():
    """
    Displays the story and decisions for path 5. Checks if
    the player has the blessing.
    """
    print()
    typing("You enter a fiery room filled with pits of lava.\n\n")
    typing("In the corner of the room are some wooden planks.\n\n")
    typing("The exit to the room is on the opposite side of the lava.\n\n")
    typing(f"{player.name}: 'I need to get over to the other side "
           "somehow...'\n\n")
    if player.blessing:
        typing("You feel the power of the blessing radiating.\n\n")
        typing("It seems to protect you from the heat!\n\n")
    typing(f"{player.name}: 'Maybe I could try using those planks to get\n"
           "across?'\n\n")
    typing("How do you want to get across?\n\n")
    typing("1. Try to use the planks to build a bridge across.\n")
    typing("2. Try to go through the lava.\n")
    if player.blessing:
        typing("3. Use the power of the blessing to make it across.\n")
    lava_choice()
    typing("You wipe the sweat off your face and continue onward.\n\n")
    feast_room()
    return


def lava_choice():
    """
    Asks the player for their input on how they wish to
    cross the lava in path 5.
    Checks if the player has the blessing and gives them an
    extra option to cross.
    If the player chooses option 1, gives them a 1 in 4 chance
    to succeed in crossing.
    """
    if player.blessing:
        cross_lava = input("Choose an option (1/2/3)\n")
    else:
        cross_lava = input("How do you wish to get across? (1/2)\n")

    if cross_lava == "1":
        typing("You take the planks from the corner of the room.\n\n")
        typing("You build a bridge to the other side.\n\n")
        typing("You begin to slowly walk along the planks...\n\n")
        time.sleep(A)
        cross_chance = random.randrange(1, 5)
        if cross_chance > 3:
            typing("You successfully make it across!\n\n")
        elif cross_chance <= 3:
            typing("A plank snaps as you walk over it!\n\n")
            typing("You fall into the pit of lava below!\n\n")
            death()
    elif cross_lava == "2":
        typing(f"{player.name}: 'Maybe it's just fake lava..?'\n\n")
        typing("You try to go through the lava without protection.\n\n")
        typing(f"{player.name}: 'Oh God! This was a bad idea!'\n\n")
        typing("The lava begins to burn you to a crisp!\n\n")
        death()
    elif cross_lava == "3" and player.blessing:
        typing("You use the power of the blessing to protect you.\n\n")
        typing("You walk through the lava and don't feel a thing!\n\n")
        typing(f"{player.name}: 'Wow! That was like walking on air!'\n\n")
        typing("You feel the power of the blessing fade...\n\n")
        player.blessing = False
    return


def feast_room():
    """
    Displays the story and decisions for the feast room.
    Checks if the player still has the blessing.
    """
    print()
    typing("You enter a grand room with a large opulant table.\n\n")
    typing("On the table is all sorts of food and drink.\n\n")
    typing("It looks like the food has been freshly served.\n\n")
    typing(f"{player.name}: 'Everything looks so delicious!'\n\n")
    typing("You approach the table and your stomach begins to growl.\n\n")
    if player.blessing:
        typing("You sense that some of the food is poisoned.\n\n")
        typing("You feel the power of the blessing at work and identify the "
               "poisoned food.\n\n")
        typing(f"{player.name}: 'I'll have some of the tasty, non-poisoned\n"
               "food thanks!'\n\n")
        typing("As you begin to eat, the power of the blessing fades...\n\n")
        player.blessing = False
    else:
        typing("A sudden urge to eat overcomes you and you sit down to "
               "feast.\n\n")
        typing(f"{player.name}: 'I'm starving!'\n\n")
        typing("On the table is a steak, soup, apples and chicken.\n\n")
        food_choice()
    typing(f"{player.name}: 'Everything tastes so delicious!'\n\n")
    typing("You continue to eat, and feel the urge to keep going.\n\n")
    eating_choice()
    typing("You get up from the table and head towards the next room.\n\n")
    chest_room()
    return


def food_choice():
    """
    Asks the user for their input on what food they wish
    to eat. Runs a random chance to eat poisoned food.
    3/4 chance to eat poison food and 1/4 chance to not.
    """
    eat_food = input("What food do you wish to eat?\n")

    if eat_food.lower().strip() == "steak":
        typing("You take a bite of the steak...\n\n")
    elif eat_food.lower().strip() == "soup":
        typing("You drink some of the soup...\n\n")
    elif eat_food.lower().strip() == "apple":
        typing("You eat an apple...\n\n")
    elif eat_food.lower().strip() == "chicken":
        typing("You eat a piece of chicken...\n\n")
    else:
        print("Please type steak, soup, apple or chicken!")
        food_choice()

    time.sleep(A)

    poison_chance = random.randrange(1, 5)
    if poison_chance > 3:
        typing(f"The {eat_food} was delicious!\n\n")
    elif poison_chance <= 3:
        typing(f"The {eat_food} causes you to heave!\n\n")
        typing("It seems that it was poisoned!\n\n")
        typing(f"{player.name}: 'My insides feel like they are going to\n"
               "explode!'\n\n")
        typing("You fall to the floor as you begin to cough up blood!\n\n")
        death()
    return


def eating_choice():
    """
    Asks the user for their input on whether they wish to
    continue eating or stop eating for the feast room. Displays
    an output depending on their choice.
    """
    keep_eating = input("Do you want to continue eating? (Yes/No)\n")

    if keep_eating.lower().strip() == "yes":
        typing(f"{player.name}: 'Can't stop now... I'm too hungry!'\n\n")
        time.sleep(A)
        end_2()
    elif keep_eating.lower().strip() == "no":
        typing(f"{player.name}: 'No... I must continue on to the treasure!'"
               "\n\n")
        typing("You decide to stop eating.\n\n")
    else:
        print("Please type Yes or No!")
        eating_choice()
    return


def statue_room():
    """
    Displays the story and decisions for the statue room.
    """
    print()
    typing("You enter a room with 3 large imposing statues.\n\n")
    typing("Two of the statues are holding weapons but one is not.\n\n")
    typing("There is a table in front of you with 3 stone weapons on it.\n\n")
    typing("They appear to be an axe, a sword and a bow.\n\n")
    typing(f"{player.name}: 'What if I place a weapon on the odd statue?'\n\n")
    statue_choice()
    time.sleep(A)
    typing("A rumbling can be heard...\n\n")
    typing("The doorway ahead opens!\n\n")
    typing("You head through to the next area.\n\n")
    key_room()
    return


def statue_choice():
    """
    Displays the random weapon combo for the statues.
    Checks the user input against the statue combos and
    prints the output depending on whether they were correct
    or not.
    """
    typing(f"{player.name}: 'The two statues with weapons are holding a\n"
           f"{random_select.weapons}.'\n\n")
    typing(f"{player.name}: 'What should I take from the table?'\n\n")
    weapon_choice = input("Axe, Sword or Bow?\n")

    while True:
        if (weapon_choice.lower().strip() == "axe" and
                random_select.weapons == "Bow and Sword"):
            typing("You take the Axe and put it on the statue...\n\n")
            break
        elif (weapon_choice.lower().strip() == "sword" and
                random_select.weapons == "Bow and Axe"):
            typing("You take the Sword and put it on the statue...\n\n")
            break
        elif (weapon_choice.lower().strip() == "bow" and
                random_select.weapons == "Sword and Axe"):
            typing("You take the Bow and put it on the statue...\n\n")
            break
        else:
            if (weapon_choice.lower().strip() == "axe" or
                    weapon_choice.lower().strip() == "bow" or
                    weapon_choice.lower().strip() == "sword"):
                typing(f"You take the {weapon_choice} and put it on the "
                       "statue...\n\n")
                typing("Nothing seems to happen...\n\n")
                time.sleep(A)
                typing("Suddenly, the statues come to life!\n\n")
                typing(f"{player.name}: 'Oh no! I messed up!'\n\n")
                typing("The statues get closer and you try to run...\n\n")
                typing("You trip over on a piece of rock!\n\n")
                typing("Everything fades to black as the sound of stone "
                       "footsteps get closer...\n\n")
                death()
                break
            else:
                weapon_choice = input("Please enter Axe, Sword or Bow!\n")
    return


def key_room():
    """
    Displays the story for the key room.
    """
    print()
    typing("You enter a tiny room illuminated by a glowing white crystal "
           "above.\n\n")
    typing("In the centre of the room is a pedestal shaped like 2 hands.\n\n")
    typing(f"{player.name}: 'This room feels different to the others.'\n\n")
    typing(f"{player.name}: 'It's so calm and peaceful...'\n\n")
    typing(f"{player.name}: 'But I can't let down my guard yet.'\n\n")
    typing("You approach the pedestal and notice a small gold key upon it."
           "\n\n")
    typing("A faint humming noise can be heard from the key.\n\n")
    typing(f"{player.name}: 'This key seems like it may be important...'\n\n")
    key_choice()
    typing("You continue through the tomb to the next area.\n\n")
    chest_room()
    return


def key_choice():
    """
    Asks the player for input on taking the gold key.
    Displays an outcome depending on their choice. Adds
    the key to player inventory if they input yes.
    """
    key_take = input("Do you want to take the key? (Yes/No)\n")

    if key_take.lower().strip() == "yes":
        typing("You slowly reach forward for the key...\n\n")
        typing("You carefully take the key from the pedestal.\n\n")
        typing("You obtained a gold key!\n\n")
        player.key = True
    elif key_take.lower().strip() == "no":
        typing(f"{player.name}: 'This could be a trap...\n"
               "I think I'll leave it.'\n\n")
        typing("You decide not to take the key.\n\n")
    else:
        print("Please type Yes or No!")
        key_choice()
    return


def chest_room():
    """
    Displays the story for the chest room.
    """
    print()
    typing("You walk into a grand circular room.\n\n")
    typing("Surrounding the room are great marble pillars.\n\n")
    typing("You spot something in the centre of the room.\n\n")
    typing(f"{player.name}: 'Could it be?'\n\n")
    typing("A grand golden chest rests in the centre of the room.\n\n")
    typing("It is decorated with golden leaves, each worth a fortune.\n\n")
    typing(f"{player.name}: 'This must be it! The Treasure of Mazar!'\n\n")
    typing("It seems your journey is almost over.\n\n")
    typing("A gold lock seals the chest shut.\n\n")
    typing("And it is far too heavy to carry.\n\n")
    typing("You will need to open it here to get the treasure inside.\n\n")
    typing(f"{player.name}: 'The lock seems pretty complex...'\n\n")
    if player.key:
        typing(f"{player.name}: 'Hmm, I wonder if that gold key fits?'\n\n")
    chest_choice()
    typing("You slowly open the chest...\n\n")
    time.sleep(A)
    typing(f"{player.name}: 'No way... I must be dreaming!'\n\n")
    typing("Inside the chest rests an immaculate gold chalice.\n\n")
    typing("The chalice is encrusted with countless jewels.\n\n")
    typing("You pick up the chalice and hold it above your head.\n\n")
    typing(f"{player.name}: 'I found the Treasure of Mazar!'\n\n")
    typing("However, your celebration is cut short as a rumbling is felt.\n\n")
    typing("Pieces of rock begin to fall as the tomb starts to collapse!\n\n")
    typing(f"{player.name}: 'Oh no! I better get out of here!'\n\n")
    if player.secret:
        typing("You remember the secret exit Arlay told you about.\n\n")
        typing("You have 3 options to choose from:\n\n")
    else:
        typing("You have 2 options to choose from:\n\n")
    typing("1. Escape from the way you came.\n")
    typing("2. Stay where you are and wait.\n")
    if player.secret:
        typing("3. Use the secret exit.\n")
    escape_choice()
    end_4()
    return


def chest_choice():
    """
    Asks the player for input on opening the chest in
    the chest room.
    If yes, opens the chest with a 1 in 3 chance of success.
    If yes and has the key, opens the chest and loses the key.
    If no, runs the end_3 function.
    """
    open_chest = input("Try to open the chest? (Yes/No)\n")

    if open_chest.lower().strip() == "yes" and player.key is False:
        typing("You attempt to pick the lock on the chest...\n\n")
        typing("The mechanism feels ancient...\n\n")
        time.sleep(A)
        open_chance = random.randrange(1, 4)
        if open_chance > 2:
            typing("Suddenly, you hear a click!\n\n")
            typing("You manage to pick the lock!\n\n")
        elif open_chance <= 2:
            typing("The lock seizes as you attempt to open it.\n\n")
            typing("Suddenly, all exits of the room close!\n\n")
            typing(f"{player.name}: 'No! I came so far!'\n\n")
            typing("The chest sinks into a platform below ground.\n\n")
            typing("The floor and ceiling start moving toward each other!\n\n")
            typing("You lie down, defeated, as you await the inevitable..."
                   "\n\n")
            time.sleep(A)
            death()
    elif open_chest.lower().strip() == "yes" and player.key:
        typing("You pull out the gold key you found earlier.\n\n")
        typing("You insert it into the lock.\n\n")
        typing(f"{player.name}: 'Please don't be a fake...'\n\n")
        time.sleep(A)
        typing("Success! The key opens the lock!\n\n")
        player.key = False
    elif open_chest.lower().strip() == "no":
        typing(f"{player.name}: 'It might be a trap...'\n\n")
        typing("You look at the gold leaves decorating the chest.\n\n")
        typing(f"{player.name}: 'These gold leaves would set me for life...'"
               "\n\n")
        typing("You cut the gold leaves off the chest.\n\n")
        typing(f"{player.name}: 'I'm more than happy with this.'\n\n")
        end_3()
    else:
        print("Please type Yes or No!")
        chest_choice()
    return


def escape_choice():
    """
    Asks the user for input on escaping the tomb. Displays
    an outcome depending on their choice. If user chooses 1,
    rolls a 1 in 3 chance of successfully escaping.
    """
    if player.secret:
        escape = input("Please select an option. (1/2/3)\n")
    else:
        escape = input("Please select an option. (1/2)\n")

    if escape.strip() == "1":
        typing(f"{player.name}: 'I better get out of here quick!'\n\n")
        typing("You start to run back the way you came in...\n\n")
        typing("You keep running and running as the tomb collapses...\n\n")
        typing("It feels like you're running a marathon.\n\n")
        escape_chance = random.randrange(1, 4)
        if escape_chance > 2:
            typing("You manage to narrowly avoid debris!\n\n")
            typing("You see some light shining through ahead!\n\n")
            typing(f"{player.name}: 'That must be the exit!'\n\n")
            typing("It seems that the doors to the tomb have fallen apart!"
                   "\n\n")
            typing("You make a final sprint to the exit...\n\n")
            typing("And come out unscathed!\n\n")
        elif escape_chance <= 2:
            typing("You are struck by a piece of falling debris!\n\n")
            typing("Your legs become stuck under the debris.\n\n")
            typing(f"{player.name}: 'No! Please! I was so close!'\n\n")
            typing("You try to move from under the debris...\n\n")
            typing("But can't move yourself!\n\n")
            typing("More debris falls around you...\n\n")
            typing(f"{player.name}: 'What did I do to deserve this?'\n\n")
            typing("A large boulder falls on top of you!\n\n")
            time.sleep(A)
            death()
    elif escape.strip() == "2":
        typing("You choose to stay and wait.\n\n")
        typing(f"{player.name}: 'Maybe if I wait, it might stop collapsing?'"
               "\n\n")
        typing("More and more debris falls in the tomb.\n\n")
        typing("Soon, the pillars supporting the room collapse!\n\n")
        typing(f"{player.name}: 'Maybe this wasn't such a good idea...'\n\n")
        typing("The room collapses and you are crushed!\n\n")
        time.sleep(A)
        death()
    elif escape.strip() == "3" and player.secret:
        typing("You head for the secret exit!\n\n")
        typing(f"{player.name}: 'I hope Arlay was telling the truth!'\n\n")
        typing("You find a secret passageway behind a pillar!\n\n")
        typing(f"{player.name}: 'This must be it!'\n\n")
        typing("You head down the secret passage...\n\n")
        typing("It's long and winding, but it's stable.\n\n")
        typing("Soon, you see daylight ahead.\n\n")
        typing(f"{player.name}: 'That must be the exit!'\n\n")
        typing("You head toward the light...\n\n")
        typing("And find yourself outside!\n\n")
    else:
        if player.secret:
            print("Please type 1, 2 or 3!")
        else:
            print("Please type 1 or 2!")
        escape_choice()
    return


def create_riddle():
    """
    Stores a list of riddles.
    """
    riddle_list = [
        "'I am tallest at the beginning of my life, "
        "but shortest at its end.'\n",
        "'I am always in front of you, but can't be seen.'\n",
        "'Always in you, sometimes on you; If I surround "
        "you, I can kill you.'\n",
        "'I cause death yet make your day. I am your friend, "
        "but your enemy.\n I am the beginning and end.'\n",
        "'Crimson I am born, yellow I dance, ebony I die.'\n",
        "'I can fly but I have no wings. I can cry but I "
        "have no eyes.'\n",
        "'I'm light as a feather, yet the strongest man can't "
        "hold me for more than\n 5 minutes.'\n"
    ]

    return riddle_list


def riddle_choice():
    """
    Displays the random riddle and gets input from
    the user, and checks the player answer against
    the correct answer. Displays an outcome depending
    on if the answer is correct or not.
    """
    riddle = create_riddle()
    random_select.riddle = random.choice(riddle)

    print(Fore.CYAN)
    typing(random_select.riddle)
    print(Fore.RED + Style.BRIGHT)
    riddle_answer = input("'What am I?'\n")

    print(Style.RESET_ALL)
    if ("candle" in riddle_answer.lower().strip() and
            random_select.riddle == riddle[0]):
        typing("Correct!\n\n")
    elif ("future" in riddle_answer.lower().strip() and
            random_select.riddle == riddle[1]):
        typing("Correct!\n\n")
    elif ("water" in riddle_answer.lower().strip() and
            random_select.riddle == riddle[2]):
        typing("Correct!\n\n")
    elif ("time" in riddle_answer.lower().strip() and
            random_select.riddle == riddle[3]):
        typing("Correct!\n\n")
    elif ("fire" in riddle_answer.lower().strip() and
            random_select.riddle == riddle[4]):
        typing("Correct!\n\n")
    elif ("cloud" in riddle_answer.lower().strip() and
            random_select.riddle == riddle[5]):
        typing("Correct!\n\n")
    elif ("breath" in riddle_answer.lower().strip() and
            random_select.riddle == riddle[6]):
        typing("Correct!\n\n")
    else:
        print(Fore.RED + Style.BRIGHT)
        typing("'YOU FOOL... You are not worthy to pass!'\n")
        print(Style.RESET_ALL)
        typing("Suddenly a great flash of light envelopes the room.\n\n")
        typing("Intense heat begins to burn your flesh...\n\n")
        typing("Until nothing remained but ash.\n\n")
        time.sleep(A)
        death()
    return


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
    return


def death():
    """
    Displays the death message.
    """
    print()
    print(Fore.RED + Style.BRIGHT + ascii_art.DEATH)
    print(Style.RESET_ALL)
    print("Better luck next time!\n")
    try_again()
    return


def end_1():
    """
    Displays ending 1.
    """
    print()
    typing("You decide to turn back and live another day.\n\n")
    typing("The treasure was tempting, but it wasn't worth risking your "
           "life.\n\n")
    typing("You make your way back home to your family and friends.\n\n")
    typing("And think about what the future has in store for you...\n\n")
    print("""
     ________________________
    |                        |
    |        ENDING 1        |
    |   -No Price on Life-   |
    |________________________|
    """)
    try_again()
    return


def end_2():
    """
    Displays ending 2.
    """
    print()
    typing("You continue stuffing your mouth with food...\n\n")
    typing("The food seems to magically refill itself after you eat it.\n\n")
    typing("More and more, you eat and eat...\n\n")
    typing("Until you forget the reason you came here in the first place.\n\n")
    typing("The only thing on your mind is to keep eating...\n\n")
    typing(f"{player.name}: 'Have to keep eating... Still hungry!'\n\n")
    print()
    typing("Outside the tomb, rumours spread of a ravenous beast.\n\n")
    typing("One that inhabits the tomb and feasts on those who dare enter."
           "\n\n")
    typing("It is said that you can hear it feasting from the entrance...\n\n")
    typing("None dared to enter the tomb out of fear of being its next meal."
           "\n\n")
    print("""
     ________________________
    |                        |
    |        ENDING 2        |
    |   -Curse of Hunger-    |
    |________________________|
    """)
    try_again()
    return


def end_3():
    """
    Displays ending 3.
    """
    print()
    typing("Happy with the golden leaves, you leave the tomb.\n\n")
    typing("The treasure was close, but would you have survived afterwards?"
           "\n\n")
    typing("You take the leaves back to your town.\n\n")
    typing("Nobody had seen such intricate crafting before.\n\n")
    typing("You managed to take them to the market and sell them for a small "
           "fortune.\n\n")
    typing("Though none believed your tales of the tomb.\n\n")
    typing("You and your family moved to the city with the riches you made."
           "\n\n")
    typing("And began living a life of luxury that you always dreamed of.\n\n")
    print("""
     ________________________
    |                        |
    |        ENDING 3        |
    |   -A Humble Future-    |
    |________________________|
    """)
    try_again()
    return


def end_4():
    """
    Displays ending 4.
    """
    print()
    typing("You look down at the glistening gold chalice.\n\n")
    typing("After hundreds of years, the Treasure of Mazar was found.\n\n")
    typing("And it was held firmly in your grasp!\n\n")
    typing("You smile, thinking of the possibilities.\n\n")
    typing(f"{player.name}: 'I could be named a lord for finding this!'\n\n")
    typing(f"{player.name}: 'I'll be called the greatest explorer!'\n\n")
    typing(f"{player.name}: 'But first, let me get home...'\n\n")
    typing(f"{player.name}: 'I'm exhausted!'\n\n")
    typing("You make your way back home with your prize in hand.\n\n")
    typing("And rest up after an exhausting adventure.\n\n")
    typing("A day later, you travel to the capital.\n\n")
    typing("All eyes on you as you carry the fabled treasure with you.\n\n")
    typing("After seeking audience with the King, you display the chalice."
           "\n\n")
    typing("And are granted lordship for your endeavours.\n\n")
    typing("The people look to you as a hero.\n\n")
    typing("And your name is spoken with reverence.\n\n")
    typing(f"{player.name}! The name that will be recorded for all history!"
           "\n\n")
    typing("But does your journey end here?\n\n")
    typing("Who knows what other treasures lay hidden...\n\n")
    typing("Waiting to be found...\n\n")
    typing(f"{player.name}: 'Whatever else is out there... I'll find it!'\n\n")
    typing("To be continued...?\n\n")
    time.sleep(A)
    print("""
     ________________________
    |                        |
    |        ENDING 4        |
    |   -Treasure of Mazar-  |
    |________________________|
    """)
    print(Fore.YELLOW + "Congratulations! You found the Treasure of Mazar!")
    print(Fore.RESET)
    print("Did you find the other 3 endings?\n")
    try_again()
    return


introduction()
