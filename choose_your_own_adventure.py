name = input("Enter your name: ")
print(f"Welcome {name} to this adventure!")

answer = input(
    "You are on dirt road it has come to an end and you can go left or right.which way you would like to go? ").lower()
 

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type to walk around and swim to swim across: ").lower()
    if answer == "swim":
        print("You swam and got eaten by an alligator.")
    elif answer == "walk": 
        print("You walked for many miles and ran out of water ultmately made you lose.")
    else:               
        print("Not a valid option.")
elif answer == "right":
    print()
else:
    print("Not a valid option.")