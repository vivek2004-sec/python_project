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

guess = int(input("Please make a guess: "))

while random_number == guess:
    print("Whoa! your guess is correct.")
    break

print("Sorry, the number is ->",random_number)
print("Better Luck next time.")