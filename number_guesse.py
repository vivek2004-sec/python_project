import random


def get_top_of_range() -> int:
    top_of_range = (input("Enter the number: "))
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("please enter larger number.")
            quit()
    else:
         print("Please enter valid number.")
         quit()
    return get_top_of_range()


# print(get_top_of_range())