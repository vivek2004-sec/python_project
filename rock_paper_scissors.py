import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Please enter rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # rock : 0 , paper : 1, scissors : 3
    computer_pick = options[random_number]
    print("Computet:",computer_pick)
    
    
    
    if computer_pick ==  user_input:
        print("It's a tie.")
        continue
    
    if computer_pick == "rock" and user_input == "paper":
        print("You Won.")
        break
    
    if  computer_pick == "rock" and user_input == "scissors":
        print("You lost.")
        break
    
    if computer_pick == "paper" and user_input == "rock":
        print("You lost.")
        break
    
    if computer_pick == "paper" and user_input == "scissors":
        print("You won.")
        break
    
    if computer_pick == "scissors" and user_input == "paper":
        print("You lost.")
        break
    
    if computer_pick == "scissors" and user_input == "rock":
        print("You won.")
        break
    
    
    
print("Goodbye!")


    

