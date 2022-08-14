import random
import time
import sys
import os


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
    room.
    """
    def __init__(self, weapons, riddle):
        self.weapons = weapons
        self.riddle = riddle


random_select = Random('', '')



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
    player.key = False
    player.blessing = False
    player.secret = False
    weapon_combos = ['Sword and Axe', 'Bow and Sword', 'Bow and Axe']
    random_select.weapons = random.choice(weapon_combos)
    create_riddle()

    start_choice = input("Are you ready to start your adventure? (Yes/No)\n")
    if start_choice.lower().strip() == "yes":
        player.name = input("What is your name?\n")
        if len(player.name.strip()) > 0 and len(player.name.strip()) <= 30:
            print(f"Welcome {player.name}. Your adventure awaits!\n")
            begin_adventure()
        else:
            print("Your name must be more than 0 characters and no more than 30!")
            start_game()
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
    door_choice()
    riddle_choice()
    print("'Impressive, mortal... You are wise indeed!'\n")
    print("'Take my blessing and venture forth! Your treasure lies deeper.'\n")
    player.blessing = True
    print(f"{player.name}: 'Um, thank you. Talking... Stone face?'\n")
    print("The great door opens before you and you carefully go through.\n")
    print("As you travel onward, you come to another crossroad!\n")
    print("To the left, you notice an orange glow and an intense wave of heat.\n")
    print("To the right, you feel a cold chill and an ominious presence.\n")
    path_choice()
    

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
    Displays the story and decisions for path 3.
    """
    print()
    print("You enter a large dark room illuminated only by your torch.\n")
    print("Cold air chills you to the bone and you feel uneasy.\n")
    print(f"{player.name}: 'Brrr! It's freezing in here. Even my torch feels cold.'\n")
    print("As you make your way through the room, you feel like you're being watched.\n")
    print("Frost has formed on the floor making it hard to walk on.\n")
    print("Out of the corner of your eye, you spot a ghostly figure.\n")
    print("It watches you intently, almost as if it's beckoning you over.\n")
    print(f"{player.name}: 'Yikes, that's unsettling...'\n")
    ghost_choice()
    print("You continue your adventure deeper into the tomb...\n")
    feast_room()

    

def path_4():
    """
    Displays the story and decisions for path 4. Checks if
    the player has picked up the dagger.
    """
    print()
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
    Displays the story and decisions for path 5.
    """
    print()
    print("You enter a fiery room filled with pits of lava.\n")
    print("In the corner of the room are some wooden planks.\n")
    print("The exit to the room is on the opposite side of the lava.\n")
    print(f"{player.name}: 'I need to get over to the other side somehow...'\n")
    if player.blessing:
        print("You feel the power of the blessing radiating.\n")
        print("It seems to protect you from the heat!\n")
    print(f"{player.name}: 'Maybe I could try using those planks to get across?'\n")
    print("What do you want to do?\n")
    print("1. Try to use the planks to build a bridge across.\n")
    print("2. Try to go through the lava.\n")
    if player.blessing:
        print("3. Use the power of the blessing to make it across.\n")
    lava_choice()


def feast_room():
    """
    Displays the story and decisions for the feast room.
    Checks if the player still has the blessing.
    """
    print()
    print("You enter a grand room with a large opulant table.\n")
    print("On the table is all sorts of food and drink.\n")
    print("It looks like the food has been freshly served.\n")
    print(f"{player.name}: 'Everything looks so delicious!'\n")
    print("You approach the table and your stomach begins to growl.\n")
    if player.blessing:
        print("You sense that some of the food is poisoned.\n")
        print("You feel the power of the blessing at work and identify the poisoned food.\n")
        print(f"{player.name}: 'I'll have some of the tasty, non-poisoned food thanks!'\n")
        print("As you begin to eat, the power of the blessing fades...\n")
        player.blessing = False
    else: 
        print("A sudden urge to eat overcomes you and you sit down to feast.\n")
        print(f"{player.name}: 'I'm starving!'\n")
        print("On the table is a steak, soup, apples and chicken.\n")
        food_choice()
    print(f"{player.name}: 'Everything tastes so delicious!'\n")
    print("You continue to eat, and feel the urge to keep going.\n")
    eating_choice()
    print("You get up from the table and head towards the next room.\n")


def food_choice():
    """
    Asks the user for their input on what food they wish
    to eat. Runs a random chance to eat poisoned food.
    3/4 chance to eat poison food and 1/4 chance to not.
    """
    eat_food = input("What food do you wish to eat?\n")
    if eat_food.lower().strip() == "steak":
        print("You take a bite of the steak...\n")
    elif eat_food.lower().strip() == "soup":
        print("You drink some of the soup...\n")
    elif eat_food.lower().strip() == "apple":
        print("You eat an apple...\n")
    elif eat_food.lower().strip() == "chicken":
        print("You eat a piece of chicken...\n")
    else:
        print("Please type steak, soup, apple or chicken!")
        food_choice()
    
    poison_chance = random.randrange(1, 5)
    if poison_chance > 3:
        print(f"The {eat_food} was delicious!\n")
    elif poison_chance <= 3:
        print(f"The {eat_food} causes you to heave!\n")
        print("It seems that it was poisoned!\n")
        print(f"{player.name}: 'My insides feel like they are going to explode!'\n")
        print("You fall to the floor as you begin to cough up blood!")
        death()


def eating_choice():
    """
    Asks the user for their input on whether they wish to
    continue eating or stop eating for the feast room. Displays
    an output depending on their choice.
    """
    keep_eating = input("Do you want to continue eating? (Yes/No)\n")
    if keep_eating.lower().strip() == "yes":
        print(f"{player.name}: 'Can't stop now... I'm too hungry!'\n")
        end_2()
    elif keep_eating.lower().strip() == "no":
        print(f"{player.name}: 'No... I must continue on to the treasure!'\n")
        print("You decide to stop eating.\n")
    else:
        print("Please type Yes or No!")
        eating_choice()


def door_choice():
    """
    Asks the user for their input on whether they wish to
    open the door in path 1 and displays an output depending
    on their choice.
    """
    open_door = input("Open the door? (Yes/No)\n")
    if open_door.lower().strip() == "yes":
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
        print(f"{player.name}: 'I guess I have no choice...'\n")
        print(f"{player.name}: 'What is your riddle?'\n")
        print("'Answer me this:'\n")
    elif open_door.lower().strip() == "no":
        print(f"{player.name}: 'I think I preferred the other room...'\n")
        print("You decide to turn around and head back to the room with pots.\n")
        path_2()
    else:
        print("Please type Yes or No!")
        door_choice()


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
        sneak_chance = random.randrange(1, 5)
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
    key_room()


def statue_choice():
    """
    Displays the random weapon combo for the statues.
    Checks the user input against the statue combos and
    prints the output depending on whether they were correct
    or not.
    """
    print(f"{player.name}: 'The two statues with weapons are holding a {random_select.weapons}.'\n")
    print(f"{player.name}: 'What should I take from the table?'\n")
    weapon_choice = input("Axe, Sword or Bow?\n")
    if weapon_choice.lower().strip() == "axe" and random_select.weapons == "Bow and Sword":
        print("You take the Axe and put it on the statue...\n")
    elif weapon_choice.lower().strip() == "sword" and random_select.weapons == "Bow and Axe":
        print("You take the Sword and put it on the statue...\n")
    elif weapon_choice.lower().strip() == "bow" and random_select.weapons == "Sword and Axe":
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


def key_room():
    """
    Displays the story for the key room.
    """
    print()
    print("You enter a tiny room illuminated by a glowing white crystal above.\n")
    print("In the centre of the room is a pedestal shaped like 2 hands.\n")
    print(f"{player.name}: 'This room feels different to the others.'\n")
    print(f"{player.name}: 'It's so calm and peaceful...'\n")
    print(f"{player.name}: 'But I can't let down my guard yet.'\n")
    print("You approach the pedestal and notice a small gold key upon it.\n")
    print("A faint humming noise can be heard from the key.\n")
    print(f"{player.name}: 'This key seems like it may be important...'\n")
    key_choice()
    print("You continue through the tomb to the next area.\n")


def key_choice():
    """
    Asks the player for input on taking the gold key.
    Displays an outcome depending on their choice.
    """
    key_take = input("Do you want to take the key? (Yes/No)\n")
    if key_take.lower().strip() == "yes":
        player.key = True
        print("You slowly reach forward for the key...\n")
        print("You carefully take the key from the pedestal.\n")
        print("You obtained a gold key!\n")
    elif key_take.lower().strip() == "no":
        print(f"{player.name}: 'This could be a trap... I think I'll leave it.'\n")
        print("You decide not to take the key.\n")
    else:
        print("Please type Yes or No!")
        key_choice()


def create_riddle():
    """
    Generates a random riddle from a list.
    """
    riddle_list = [
        "'I am tallest at the beginning of my life, but shortest at its end.'\n",
        "'I am always in front of you, but can't be seen.'\n",
        "'Always in you, sometimes on you; If I surround you, I can kill you.'\n",
        "'I cause death yet make your day. I am your friend, but your enemy. I am the beginning and end.'\n",
        "'Crimson I am born, yellow I dance, ebony I die.'\n",
        "'I can fly but I have no wings. I can cry but I have no eyes.'\n",
        "'I'm light as a feather, yet the strongest man can't hold me for more than 5 minutes.'\n"
    ]

    random_select.riddle = random.choice(riddle_list)


def riddle_choice():
    """
    Displays the random riddle and gets input from
    the user, and checks the player answer against
    the correct answer.
    """
    print(random_select.riddle)
    riddle_answer = input("'What am I?'\n")
    if "candle" in riddle_answer.lower().strip() and random_select.riddle == "'I am tallest at the beginning of my life, but shortest at its end.'\n":
        print("Correct!\n")
    elif "future" in riddle_answer.lower().strip() and random_select.riddle == "'I am always in front of you, but can't be seen.'\n":
        print("Correct!\n")
    elif "water" in riddle_answer.lower().strip() and random_select.riddle == "'Always in you, sometimes on you; If I surround you, I can kill you.'\n":
        print("Correct!\n")
    elif "time" in riddle_answer.lower().strip() and random_select.riddle == "'I cause death yet make your day. I am your friend, but your enemy. I am the beginning and end.'\n":
        print("Correct!\n")
    elif "fire" in riddle_answer.lower().strip() and random_select.riddle == "'Crimson I am born, yellow I dance, ebony I die.'\n":
        print("Correct!\n")
    elif "cloud" in riddle_answer.lower().strip() and random_select.riddle == "'I can fly but I have no wings. I can cry but I have no eyes.'\n":
        print("Correct!\n")
    elif "breath" in riddle_answer.lower().strip() and random_select.riddle == "'I'm light as a feather, yet the strongest man can't hold me for more than 5 minutes.'\n":
        print("Correct!\n")
    else:
        print("'YOU FOOL... You are not worthy to pass!'\n")
        print("Suddenly a great flash of light envelopes the room.\n")
        print("Intense heat begins to burn your flesh...\n")
        print("Until nothing remained but ash.\n")
        death()


def ghost_choice():
    """
    Asks the user for input on approaching the ghost.
    Displays an outcome depending on their choice.
    """
    approach_ghost = input("Approach the figure? (Yes/No)\n")
    if approach_ghost.lower().strip() == "yes":
        print("You decide to approach the ominious figure...\n")
        print(f"{player.name}: 'Hello? Can you hear me?'\n")
        print(f"???: '{player.name} why have you come?'\n")
        print("You feel a chill as the figure speaks.\n")
        print(f"{player.name}: 'How do you know my name?'\n")
        print("???: 'I know the name of all who enter this tomb.'\n")
        print(f"???: 'Now Answer me {player.name}: Why have you come?'\n")
        print("You're unsure how this figure may react to you coming for the treasure.\n")
        truth_choice()
    elif approach_ghost.lower().strip() == "no":
        print(f"{player.name}: 'I'll pretend I didn't see that.\n")
        print("You decide to continue your journey.\n")
        print("As you walk on, you begin to get colder and colder...\n")
        print("Your legs begin to seize in the freezing cold...\n")
        print("And you fall to the ground, unable to breathe.\n")
        print("You hear an ominious voice just before your senses fail.\n")
        print(f"???: 'You cannot escape fate {player.name}...'\n")
        death()
    else:
        print("Please type Yes or No!")
        ghost_choice()


def truth_choice():
    """
    Asks the user for input on telling the truth.
    Displays an outcome depending on their choice.
    """
    tell_truth = input(f"{player.name}: 'Should I tell it the truth?' (Yes/No)\n")
    if tell_truth.lower().strip() == "yes":
        print(f"{player.name}: 'I have come seeking the Treasure of Mazar.'\n")
        print("The figure stares at you, making you feel more uneasy.\n")
        print(f"???: 'I sense truth in your words {player.name}.'\n")
        print("???: 'After all, that is the reason for all who come here.\n")
        print("???: 'My name is Arlay, and I was once the architect of this tomb.'\n")
        print("Arlay: 'But I was killed here after its completion.'\n")
        print("Arlay: 'King Mazar betrayed me and cursed my soul to wander here.'\n")
        print("Arlay: 'I have long awaited someone to make it this far.'\n")
        print(f"Arlay: 'You, {player.name}, are the only one who has.'\n")
        print("Arlay: 'Allow me to tell you the secret of this place.'\n")
        print("Arlay: 'So that you may find what you seek and leave unharmed.'\n")
        print(f"{player.name}: 'Okay, but why help me?'\n")
        print("Arlay: 'So that I can have my revenge on King Mazar...'\n")
        print("Arlay: 'Listen closely.'\n")
        print("Arlay: 'When you take the treasure, the tomb is set to collapse.'\n")
        print("Arlay: 'You can exit from where you came if you are lucky.'\n")
        print("Arlay: 'But there is a secret exit in the treasure room.'\n")
        print("Arlay: 'Go through the secret exit and you will be safe.'\n")
        print("You make a note of the secret exit.\n")
        player.secret = True
        print(f"{player.name}: 'Thank you Arlay. I won't let you down!'\n")
    elif tell_truth.lower().strip() == "no":
        print(f"{player.name}: 'I am just exploring!'\n")
        print("The figure stares at you, and you feel a chill down your spine.\n")
        print("???: 'LIES!'\n")
        print("The figure lets out a piercing scream, causing your ears to ring.\n")
        print("You start feeling nauseous as the room starts to spin.\n")
        print("You collapse on the floor and hear a voice.\n")
        print(f"???: 'You are a fool {player.name}. Lies do not get past me.'\n")
        death()
    else:
        print("Please type Yes or No!")
        truth_choice()


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
    print()
    print("You continue stuffing your mouth with food...\n")
    print("The food seems to magically refill itself after you eat it.\n")
    print("More and more, you eat and eat...\n")
    print("Until you forget the reason you came here in the first place.\n")
    print("The only thing on your mind is to keep eating...\n")
    print(f"{player.name}: 'Have to keep eating... Still hungry!'\n")
    print()
    print("Outside the tomb, rumours spread of a ravenous beast.\n")
    print("One that inhabits the tomb and feasts on those who dare enter.\n")
    print("It is said that you can hear it feasting from the entrance...\n")
    print("None dared to enter the tomb out of fear of being its next meal.\n")
    print("------ENDING 2------\n")
    try_again()


def end_3():
    """
    Displays ending 3.
    """


def end_4():
    """
    Displays ending 4.
    """



introduction()