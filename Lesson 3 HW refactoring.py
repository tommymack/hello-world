import random


# Ask the user for their favorite color
greeting = input("Hello, what is your name? ")
color = input(f"What is your favorite color {greeting}? ").casefold().capitalize()

# Remember string methods to make this check easier!
# Here is where I veered off the assignment

colorlist = ["Red", "Green", "Blue", "Cyan", "Magenta", "Yellow", "Orange", "Purple"]
mycolor = random.choice(colorlist)

# Check to see if their favorite matches yours
if color == mycolor:
    print("Wow! Me too!")
# Include a condition for the user's favorite *not* matching yours    
elif color == "Green":
    print(f"Your must be a genius {greeting}.")
else:
    print(f"My favorite is {mycolor} but I like {color} too!")



gamecolor = random.choice(colorlist)

game = input(f"Would you like to guess what color I am thinking of? (Y/N) ").capitalize()
if game[0] == "Y":
    print(f"I am thinking of the color {gamecolor}")
elif game[0] == "N":
    print("Cool, have a nice day!")
else:
    print("that is not a valid answer")
