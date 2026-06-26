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
print(random_number)