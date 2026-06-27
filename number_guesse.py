import random

def top_of_range():
    top_of_range = (input("Enter the number: "))
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        while top_of_range <= 0:
           print("Please Enter larger digit.")
           continue
           random_number = random.randint(0,top_of_range)
    print(top_of_range())      
    
top_of_range()