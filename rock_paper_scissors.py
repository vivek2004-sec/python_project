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
    # rock : 0 , paper : 1, scissors : 2
    computer_pick = options[random_number]
    print("Computer:",computer_pick)
    
    
    
    if computer_pick ==  user_input:
        print("It's a tie.")
        continue
    
    elif computer_pick == "rock" and user_input == "paper":
        print("You Won.")
        user_wins += 1
    
    elif computer_pick == "paper" and user_input == "scissors":
        print("You won.")
        computer_wins +=1
        user_wins += 1
    
    elif computer_pick == "scissors" and user_input == "rock":
        print("You won.")
        computer_wins +=1
        user_wins += 1
    
    else:
        print("You lost!")
        computer_wins +=1
    
    
print("your score: ", user_wins)    
print("computer score: ", computer_wins)  

if user_wins > computer_wins:
    print("You won!")  
elif user_wins == computer_wins:
    print("It's a tie.")
else:
    print("You lost!")
    
print("Goodbye!")



    

