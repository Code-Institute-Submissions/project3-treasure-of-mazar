import random
import time
import sys


def introduction():
    """
    Opens the game with the title screen and introduction
    to the story of the game.
    """
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
    if start_choice.lower() == "yes":
        player_name = input("What is your name?\n")
        print(f"Welcome {player_name}. Your adventure awaits!\n")
    elif start_choice.lower() == "no":
        print("Very well... Please take your time.")
        time.sleep(5)
        introduction()
    else:
        print("Please type Yes or no!")
        start_game()


introduction()