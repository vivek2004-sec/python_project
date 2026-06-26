import random


top_of_range = (input("Enter a number: "))

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please enter a larger number.")
        quit()
else:
    print("Please Enter a valid digit.")
    quit()
    
    
    
random_number = random.randint(0, top_of_range)
guesses = 0



while True:
    
    guesses += 1
    guess = input("Please make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("please type a number next time.")
        continue
    

    if random_number == guess:
        print("Whoa! You got it.")
        break
        
    else:
        print("Better Luck next time.")

    
print("The number of guesses you take ->", guesses)


    