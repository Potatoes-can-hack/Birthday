import random

def bday():
    name = input("Enter your name: ")
    print("Hi", name,"I will try to predict your birthday!")
    year = 2022
    r = random.randint(0, 2022)
    age = 2022 - r
    print("You were born in", r)
    print("You are",age,"years old")
    correct = input("Is that correct? y/n ")
    if correct == "y":
        print("Thats awesome!")
        quit()
    else:
        print("Oops!, lets try again")
    print()
    bday()
bday()