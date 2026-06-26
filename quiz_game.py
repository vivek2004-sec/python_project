print("Welcome to the Quiz Game!")

playing = input("Do you want to play the game? ")

if playing != 'yes':
    quit() # It is an command used to stop the interpreter, mainly in interactive sessions. terminates the programm.

import os

base_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(base_path, "quiz_game.py")