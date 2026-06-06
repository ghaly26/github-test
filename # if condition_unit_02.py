# Python Notes
#========================================================#
chair_number= int(input("Enter chair number: \n"))
# if chair number !=13:
#  print ("You win" )        
# else:
#  print ("sorry" )
if chair_number>13:
    print ("You win")
elif chair_number<13:
    print ("You win")
else:
    print ("sorry")

#========================================================#
# if condition with string && case sensitivity
#========================================================#
area = input("Choose an area (Tanta, Cairo, Alexandria): \n")
if area.upper()== "TANTA":
    print("You chose Tanta!")
    print("Tanta is nice!")
elif area.lower()== "cairo":
    print("You chose Cairo!")
    print("Cairo is amazing!")
elif area.lower() == "alexandria":
    print("You chose alexandria!")
    print("Alexandria feels like summer!")
else:
    print(f"{area} is not on our list!")

#========================================================#
# if condition with and or
#========================================================# 

name= input ("Please enter your name: \n")
password=input("Please enter your password: \n")

if name.lower() =="ibrahim" and password == "hiThere":
    print("Welcome back!")
else:
    print("Sorry, wrong name or password.")

#========================================================#
#and-or exapmle

age = int(input( "Please enter your age: \n"))
license= input ("Do you have a license? Type (Yes) or (No): \n")
if age >= 18 and license.lower() == "yes":
    print("You can drive!")
elif age <18 or license.lower() == "no":
    print("Sorry, you cannot drive without a license.")
else:
    print(f"Sorry,your entery of [{license}] is not understood.")

#========================================================#
# if condition with nested if 
#========================================================#
is_egyptian = input("Are you Egyptian? Type (Yes) or (No): \n")
if is_egyptian.lower() == "yes":
    print("Good, that's the first step")
    is_18 = input("Are you above 18? Type (Yes) or (No): \n")
    if is_18.lower() == "yes":
        print("You can have an ID")
    else:
        print("Sorry, you have to be 18 or older")
        print("Please try again when you are 18")
else:
    print("Sorry, an Egyptian ID is given only to Egyptians")

#========================================================#
# unit-03 code project
#========================================================#
print("""
██████╗░███████╗░█████╗░████████╗██╗░░██╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║░░██║  ██╔════╝░██╔══██╗████╗░████║██╔════╝
██║░░██║█████╗░░███████║░░░██║░░░███████║  ██║░░██╗░███████║██╔████╔██║█████╗░░
██║░░██║██╔══╝░░██╔══██║░░░██║░░░██╔══██║  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
██████╔╝███████╗██║░░██║░░░██║░░░██║░░██║  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
""")
print( "Welcome to my island!" )
print("There are two doors in front of you. a red door and a blue door")
door_choice= input("Which door do you want to open?").lower()
# Check user's choice   
if door_choice == "red":
    print("Great! now you entered a room.")
    print("You found three boxes: a white box, a black box, and a green box")
    box_choice = input("Which box do you want to open?").lower()
    if box_choice == "white":
        print("Congratulations! You found the treasure!")  
    elif box_choice == "black":
        print("Sorry, you found a monster! Game over.")
    elif box_choice == "green":
        print("Sorry, you found a trap! Game over.")
    else:
        print(f"Sorry, your entry of [{box_choice}] is not understood. Game over.")

elif door_choice == "blue":
    print("You chose the blue door.")
    print("Unfortunately, it's a dead end.")
else: 
    print(f"Sorry, your entry of [{door_choice}] is not understood. Game over.")

#========================================================#
# Unit-04 
#========================================================#
#random module
import nt
import random
pin_code= random.randint(1000, 9999)
user_input= input("Enter a 4-digit PIN code: ")
if len(str(user_input)) != 4:
    print("Please enter 4 digits")
elif user_input == pin_code:
    print("Success! PIN code matched.")
else:
    print("Failure! PIN code did not match.")
    print(f"The computer generated this PIN: {pin_code}")

#========================================================#
import random
print ("Welcome to the virtual coin toss game")
input ("Press Enter to start")
random_number= random.randint(0, 1)
if random_number == 0:
    print("Heads")
else:
    print("Tails")
#========================================================#
import random
print("Welcome to the Coin Guessing Game!")
print("Choose a method to toss the coin:")
print("1. Using random.random( )")
print("2. Using random.randint( )")

choice = input("Enter your choice (1 or 2): ")
if choice== "1":
    random_number=random.random()
    if random_number >= 0.5:
        computer_result= "Heads"
    else:
        computer_result= "Tails "
elif choice == "2":
    if random.randint(0, 1) == 0:
       computer_result = "Heads"
    else:
       computer_result = "Tails"
else:
    print("Invalid choice. Please select either 1 or 2.")

user_guess = input("Guess the coin toss result (Heads or Tails): ").capitalize()
if user_guess == computer_result:
    print("Congratulations! Your guess is correct.") 
else:
    print("Sorry, your guess is incorrect.")
    print(f"The computer generated: {computer_result}")

# if choice == "2":
#     random_number = random.randint(0, 1)
# else:
#     random_number = int(random.random() * 2)
# guess = input("Enter your Guess (Heads or Tails): ").upper()
# if guess == "HEADS" and random_number == 0:
#     print("Congratulations! You won!")
# elif guess == "TAILS" and random_number == 1:
#     print("Congratulations! You won!")
# else:
#     print("Sorry, you lost!")

#========================================================#
# Data Structure: List
#========================================================#
colors =[]
fav_color = input("Add the first color you like: ")
colors.append(fav_color)
choice = input("Do you want to add more colors? Yes/No: ").lower()
if choice == "yes":
    fav_color = input("Add another color to the list: ")
    colors.append(fav_color)
    print("The colors you like are: ")
    print(colors)
else:
    print("The color you like is: ")
    print(colors)

#========================================================#
# Unit-04 Code Project
#========================================================#
library = []
book = input("Enter the name of a book you own: ")
library.append(book)
print(f"Your Library:{library}")
book = input("Enter the name of another book you own (or press 'Enter' to skip): ")
if book:
    library.append(book)
    print(f"Your Library: {library}")
else:
    print("No more books added.")
wishlist = []
wish_book = input("Enter the name of a book you wish to have in the future: ")

wishlist.append(wish_book)
print(f"Your Wishlist: {wishlist}")
wish_book = input("Enter the name of another book you wish to have in the future (or press 'Enter' to skip): ")
if wish_book:
    wishlist.append(wish_book)
    print(f"Your Wishlist: {wishlist}")
else:
    print("No more books added.")

got_book = input("Have you got any of the books in your wishlist? Type the name of the book or press 'Enter' to skip: ")
if got_book:
    if got_book in wishlist:
        wishlist.remove(got_book)
        library.append(got_book)
        print(f"Congratulations! You got '{got_book}' and it's now in your library.")
        print(f"Your Library: {library}")
        print(f"Your Wishlist: {wishlist}")
    else:
        print(f"Sorry, '{got_book}' is not in your wishlist.")
else:
    print("No books added to your library.")

donated_book = input("Do you want to donate any book from your library? Type the name of the book or press 'Enter' to skip: ")
if donated_book:
    if donated_book in library:
        library.remove(donated_book)
        print(f"Thank you for donating '{donated_book}'!")
        print(f"Your Library: {library}")
    else:
        print(f"Sorry, '{donated_book}' is not in your library.")
else:
    print("No books donated.")

#========================================================#
# unit-05 code project
#========================================================#
import random
print ("Welcome to 'Whose Wallet?'")
print ("you will give me a list of names , and i will pick a person to pay")
names_string = input ("if you're ready, Enter the names seprated by a comma .., ")
names = names_string.split (", ")
length = len(names) -1
random_number = random.randint(0,length)
random_person = names [random_number]
print (f"please ask ' {random_person} ' to take his wallet out . Dinner is on him")

################## Another Way random.choice(names) #######################

# import random
# print ("Welcome to 'Whose Wallet?'")
# print ("you will give me a list of names , and i will pick a person to pay")
# names = input ("if you're ready, Enter the names seprated by a comma .., ").split(", ")
# print (f"please ask ' {random.choice(names)} ' to take his wallet out . Dinner is on him")
#========================================================#
#ex : Rabbit moving in the field 

print ("Welcom to place the rabbit\n")
field=[["\U0001F33E","\U0001F33E","\U0001F33E"],["\U0001F33E","\U0001F33E","\U0001F33E"],["\U0001F33E","\U0001F33E","\U0001F33E"]]
print( f"{field[0]} \n{field[1]} \n{field[2]}" )

print ("\nwhere should the rabbits go ? \U0001F430 \n")

position = (input("please choose a row and column "))

row = int(position[0])
column = int(position[1])

field[row-1][column-1]="\U0001F430"

print ("\n Success .....\n")

print( f"{field[0]} \n{field[1]} \n{field[2]}" )

#========================================================#
# unit-05code project [rock, paper, scissors game]
#========================================================#
print("Welcome to the Rock, Paper, Scissors game:")
confirm = input("Press Enter to continue or type (Help) for the rules\n").lower()
if confirm == "help":
    print("The rules are simple: ")
    print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
    print("You will be playing against the computer. Good luck!")
else:
    print("Let's get started!")

import random

choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(choices)
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

if user_choice not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")

else:
    print (f"You chose: \n{user_choice}")
    print (f"The computer chose: \n{computer_choice}") 

    if user_choice == computer_choice:
        print(f"It's a tie! Both you and the computer chose {user_choice}.")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    
      print(f"Your choice is {user_choice}: \ncomputer choice is {computer_choice}")
      print(f"You win! {user_choice} beats {computer_choice}.")
    else:
      print(f"Your choice is {user_choice}: \ncomputer choice is {computer_choice}") 
      print(f"You lose! {computer_choice} beats {user_choice}.")

#========================================================#
# unit-06 nest list
#========================================================#  
