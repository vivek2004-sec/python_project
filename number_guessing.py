import random


top_of_range = int(input("Enter a number: "))

random_number = random.randint(0, int(f"{top_of_range}"))
print(random_number)