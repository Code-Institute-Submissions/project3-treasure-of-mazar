import random
import time
import sys
import os


class PlayerAttributes:
    def __init__(self, name, location):
        self.name = name
        self.location = location


player = PlayerAttributes('', '')


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
    their name before beginning.
    """
    start_choice = input("Are you ready to start your adventure? (Yes/No)\n")
    if start_choice.lower().strip() == "yes":
        player.name = input("What is your name?\n")
        print(f"Welcome {player.name}. Your adventure awaits!\n")
        begin_adventure()
    elif start_choice.lower().strip() == "no":
        print("Very well... Please take your time.")
        time.sleep(5)
        os.system('cls||clear')
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
    player.location = "Tomb"
    time.sleep(5)
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
    elif path.lower().strip() == "right":
        if player.location == "Tomb":
            path_2()
        

def path_1():
    print()
    print("You enter the dim room with an imposing large door\n")
    

#def path_2():


#def path_3():


#def path_4():


#def path_5():


#def path_6():


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
    else:
        print("Please type Yes or No!")


#def death():


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


#def end_2():


#def end_3():


#def end_4():


introduction()