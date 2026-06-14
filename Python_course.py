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
# unit-06  
#========================================================#  
#loops
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in numbers:
    if x % 2 == 0:
        print(f"\n{x}")
print("\nFinished the loop successfully")

#========================================================#
attendees_input = input("Enter the number of attendees separated by commas: ")
attendees = attendees_input.split(",")

for person in attendees:
    print("\n" + person + "\n")
    response = input( "Is this person attending? (Yes/No): ")
    if response.lower() == "yes":
        print( "Attendance confirmed" )
    else:
        print( "Attendance not confirmed")
print("======")
#========================================================#
#python test script to ask user about their travel experiences
travel_list=input( "Please type the names of the countries separated by commas: ").split(",")

for country in travel_list:
    print( f" {country} " )
    visited=input( f"Have you ever visited {country} before? (yes/no): " )
    if visited == "yes":
        print(f"Hope you had a wonderful time in {country}!")
    else:
        print(f"Hope you get to visit {country} soon!")
    print("=======")  # Print a blank line for better readability
input("Press enter to exit...." )
#========================================================#
# to do list
tasks_list=input("Enter your today tasks separated by commas: \n").split(",")
done_tasks=[]
ongoing_tasks=[]

for task in tasks_list:
    print(f"\n{task}\n")

    done=input(f"Have you completed '{task.strip()}'? (yes/no): \n")
    if done.lower() == "yes":
        print(f"Great job on completing '{task}'")
        done_tasks.append(task)
    else:
        print(f"Keep working on '{task}'! You can do it!")
        ongoing_tasks.append(task)
    print("=======")  # Print a blank line for better readability

see_progress=input("Do you want to see your progress? (yes/no): \n")
if see_progress.lower() == "no":
        print("No problem! press enter to exit....")
else:
        print("\nHere is your progress:")
        print("""
                 ****Done Tasks***
              """)
        print(done_tasks)
        print("""                 
                ***Ongoing Tasks***
                """)
        print(ongoing_tasks)
        input("Press enter to exit....")
#========================================================#
print("*** Welcome to the multiplication table ***")
user_input = int(input("Enter a number: "))
print(f"Multiplication table for {user_input}:")
for i in range(1, 11):
    result = user_input * i
    print(f"{user_input} x {i} = {result}")

#========================================================#
items = []
prices = []
print("\n*****Welcome to iShop calculator*****\n")    
no_of_items = int( input( "How many items are there in your basket today? " ))
if no_of_items > 0:
    print( "\nLet's get to counting them ." )
    for i in range(0, no_of_items):
        name = input(f"Tell me the name of the item number {i+1}: ")
        price = float(input(f"What is the price of {name}\n$ "))
        items.append( name )
        prices.append( price )
    choice= input( "Would you like to see your entire basket items? " ).lower( )
    if choice == "yes":
        print( "\nHere are the items in your basket:" )
        print(items)
        see_price= input("Would you like to see how much it'll cost? "). lower( )
        if see_price == "yes":
            print( "\nBuying these items will cost: $" )
            print( sum( prices ) )
        else:
            input( "Press enter to exit" )
    else:
        input( "Press enter to exit" )
else:
    print( "Seems like you're not in the mood for shopping today" )

#========================================================#
numbers = [1, 2, 3, 4, 5]
total = 0
print ("Let's add each number to the next" )
for i in numbers:
    total += i
    print (f"---> {total}")
print (f"\nThe total number is:{total} \n")
#========================================================#

names=input("Enter your first and last names separated by commas: \n").split(", ")

abbreviated_names = []
for name in names:
    name_parts = name.split()
    print( name_parts)

    first_name = name_parts[0]
    last_name = name_parts[1]
    first_initial = first_name[0]
    last_initial = last_name[0]
    abbreviation = (first_initial + "." + last_initial + ".").upper()
    abbreviated_names.append(abbreviation)

print(abbreviated_names)
for name in abbreviated_names:
    print(name)
#========================================================#
#reversing the order of words in a sentence
sentence = input( "Enter a sentence: " )
words = sentence.split()
reversed_words = words[::-1]
print("reversed sentence:", " ".join(reversed_words) )
#========================================================#
#Unit-06 code project
#=========================================================#
import random
import string
print("welcome to the password generator!")
length = int(input("Enter the total number of characters for the password: "))
letters_count = int(input("Enter the number of letters: "))
digits_count = int(input("Enter the number of digits: "))
punctuation_count = int(input("Enter the number of punctuation characters: "))
if letters_count + digits_count + punctuation_count != length:
    print("The total number of characters does not match the sum of letters, digits, and punctuation.")
else:
    password = []
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    # password.extend(random.choices(letters, k=letters_count))
    # password.extend(random.choices(digits, k=digits_count))
    # password.extend(random.choices(punctuation, k=punctuation_count))
    # random.shuffle(password)
    # print("Generated password:", "".join(password))

    password_chars=(random. choices(letters, k=letters_count) +
                    random. choices(digits, k=digits_count) +
                    random. choices(punctuation, k=punctuation_count))
    random.shuffle(password_chars)
    print("Generated password:", "".join(password))
#========================================================#
#Unit-07
#========================================================#
# while loop
import random
print("Welcome to the Number Guessing Game!")
secret_number= random.randint(1, 10)
guess = int( input( "Guess a number between 1 and 10: " ))
while guess != secret_number:
    if guess < secret_number:
        print("Too low! Guess again.")
        guess = int( input( "Too low! Guess a number between 1 and 10: " ))
    else:
        print("Too high! Guess again.")
        guess = int( input( "Too high! Guess a number between 1 and 10: " ))
print("Congratulations! You guessed the number!")
#========================================================#
# unit-07 project: Hangman Game with while loop
#========================================================#
import random

Hangman_Stages = [
    
    r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']


words = ["good", "bad", "ugly"] 
random_word = random.choice (words)
display = ["_"] * len( random_word)
print (' ' .join(display))
# another syntax 
# display = []
# for letter in random_word:
#     display.append("_")    
# print(display)   


lives=6

guessed_letters=[]
print(Hangman_Stages[0])


while "_" in display and lives > 0:
    guessed=input ("Please guess a letter :").lower()

    if guessed in guessed_letters:
       print("You already guessed that. Try again." )
       print(f"have {lives} more tries")
       
       continue
    
    guessed_letters.append(guessed)

    if guessed not in random_word:
       lives -=1
       print (Hangman_Stages[6-lives])
    else:
       for position in range(len(random_word)):
           if random_word [position]== guessed:
              display [position] = guessed

    print (' ' .join(display))
    print (f" You have {lives} more tries")

if lives == 0 :
      print("""
            **********
             You lose!
            **********
            """)
      print(Hangman_Stages[-1])

else:
    print ( """
      **********
       YOU WIN!
      **********
           """ )
    
#========================================================#
encrypted_word = ""
#========================================================#
import string
alphabet = string.ascii_lowercase
word = input("Please type a word: ").lower()
encrypted_word = ""
for letter in word:
    original_position = alphabet.index(letter)
    new_position = original_position + 2
    encrypted_word += alphabet[new_position]
print(f"Here is the encrypted word: {encrypted_word}")

#========================================================#
# another way to encrypt the word using list comprehension
#=========================================================#
import string
alphabet = string.ascii_lowercase 
word = input("Please type a word: ").lower()
encrypted_word = ""
for letter in word:
    original_position = alphabet.index(letter)
    new_position = (original_position + 2)%26  # to solve z or y out of range index
    encrypted_word += alphabet[new_position]
print(f"Here is the encrypted word: {encrypted_word}")
# encrypted_word = "".join([alphabet[(alphabet.index(letter) + 2) % 26] for letter in word])
# print(f"Here is the encrypted word: {encrypted_word}")

#===========================================================#
# encryption with sentences not only word 
#===========================================================#
import string
alphabet = string.ascii_lowercase 
word = input("Please type a word: ").lower()
encrypted_word = ""
for letter in word:
    if letter in alphabet:
        original_position = alphabet.index(letter)
        new_position = (original_position + 2)%26  # to solve z or y out of range index
        encrypted_word += alphabet[new_position]
    else:
        encrypted_word+=letter
print(f"Here is the encrypted word: {encrypted_word}")

#==========================================================#





#==========================================================#
#Object oriented programming OOP
#==========================================================#
class Book:
    #attributes
    title=""
    author=""
    pages=0
my_book=Book()
my_book.title="origin"
my_book.author="Dan Brown"
my_book.pages=542

print(my_book.title)
print(my_book.author)
print (my_book. pages)

#same with Magic Methods
class Book:
    def __init__(self, title, author, pages):
       self.title=title
       self.author=author
       self.pages=pages

my_book=Book("origin", "Dan brown", 542)
third_book=Book("ghaly", "Youssef", 434)

print (my_book.author)
print(third_book.title)

#examples
#class name profile have users with user-name,email,language
class Profile:
    def __init__(self, name, email, language):
        self.name=name
        self.email-email
        self.language=language
        
ghaly=Profile(maka, ghali@gmail.com, arabic)
samuel=Profile(sam, idjfh@gmail.com, arabic)

print(ghaly.email)
print(samuel.email)

#another exam to def print 
class Task:
    def __init__ (self, title, description, due_date, status):
        self.title= title
        self.description= description
        self.due_date = due_date
        self.status= status
    def display_task(self):
         print(f"Title: {self.title}" )
         print (f"Description: {self.description}")
         print(f"Due Date: {self.due_date}")
         print(f"Status: {self.status}")

    def mark_as_complete(self): # to change the task status to complete
        self.status="complete"


taskl = Task("Review Syntax" , "Review how to create calss and,.....",9-10-2026, "incomplete")
taskl.display_task()
taskl.mark_as_complete()
taskl.display_task()

#another exam
class MoviesList:
    def __init__(self, Title, Director, Release_Year, Genre):
        self.Title=Title
        self.Director=Director
        self.Release_Year=Release_Year
        self.Genre=Genre

    def MOVIES_LIST(self):
        print(f"____MOVIES LIST____")
        print(f"Title: {self.Title}")
        print(f"Director: {self.Director}")
        print(f"Release_Year: {self.Release_Year}")
        print(f"Genre: {self.Genre}")

    def update_director(self,new_director):  #to make input variable
        self.Director=new_director

List_1=MoviesList("Inception", "Christ serlva", "2010", "Sci_Fi")
List_2=MoviesList("abcvs", "Cjjhjhj", "2011", "Romantic")
List_3=MoviesList("dssw", "A7A", "2011", "Romantic")

List_1.MOVIES_LIST()
List_2.update_director("jackie chan")
List_2.MOVIES_LIST()

#example for 
class User:
    def __init__(self, first_name, last_name, email, password, status='inactive'):
      self.first_name = first_name
      self.last_name= last_name
      self.email = email
      self.password= password
      self. status= status
     
def create_user():
   first_name = input("Enter your first name: ")
   last_name= input("Enter your last name: ")
   email = input("Enter your email: ")
   password = input("Enter your password: ")

   return User(first_name,last_name,email,password )
       
userl =create_user()
print(userl.first_name)

#another example :
class Recipe:
    def __init__(self, name, ingriedients, cooking_time, instructions):
        self.name= name
        self.ingrediants=ingriedients
        self.cooking_time= cooking_time
        self.instructions=instructions

    def display_receipe(self):
        print(f"Name: {self.name}")
        print(f"Ingrediants: {self.ingrediants}")
        print(f"Cooking Time: {self.cooking_time}")
        print(f"Instruction: {self.instructions}")
        print ("_" *20)

def create_recipe():
    name=input("Enter receipe name : ")
    ingrediants=input("Enter ingrediants (comma-seprated) : ")
    cooking_time=input("Enter cooking time: ")
    instructions=input("Enter cooking instructions : ")
    return Recipe(name, ingrediants,cooking_time, instructions)

print("Welcome to Recipe Collection \n")
my_recipe=create_recipe()
print("Recipe added successfully! \n")
my_recipe.display_receipe()

#another exp.

import os
import time

def clear_screen():
    os.system('cls' if os.name  == 'nt' else 'clear')
class User:
   def __init__ (self, first_name, last_name, email, password, status='inactive') :
      self.first_name = first_name
      self.last_name =last_name
      self.email = email
      self.password =password
      self.status =status

   def display_user(self) : 
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Status: {self.status}")
        print ("_" *20)

def create_user():
   first_name = input("Enter your first name: ")
   last_name= input("Enter your last name: ")
   email = input("Enter your email: ")
   password = input("Enter your password: ")

   return User(first_name,last_name,email,password )

new_users=[]

while True:
    print("\n  welcome to user management \n")
    print("\n  Choose an action: \n") 
    print("1. add new user")
    print("2. Display all users")
    print("3. Exit \n")

    choice = input("Enter your choice:")

    if choice == '1':
        new_users.append(create_user())
        print("User addess successfully!" )
        time.sleep(2)
    
    elif choice=='2':
        clear_screen()
        if new_users:
            print ("Displaying all new users ....")
            time.sleep (1)
            for i in new_users:
                i.display_user()
            time.sleep(2)
        else:
            print("sorry, do not find any user to display!")
            time.sleep(2)
    elif choice=='3':
        print("Exiting ....")
        break
    
    else:
        print("lnvalid choice! Please try again.") 

#another exam 

import os
import time

def clear_screen():
    os.system('cls' if os.name  == 'nt' else 'clear')
class Member:
   
   def __init__ (self, first_name, last_name, membership_id, membership_status='inactive') :
      self.first_name = first_name
      self.last_name =last_name
      self.membership_id=membership_id
      self.membership_status=membership_status
    

   def display_member(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Membership_id: {self.membership_id}")
        print(f"Membership_status: {self.membership_status}")
        print ("_" *20)

def create_member():
   first_name = input("Enter your first name: ")
   last_name= input("Enter your last name: ")
   membership_id=input("Enter your membership_id: ")
   membership_status= input("Enter your membership status or press Enter: ")
   if not membership_status:
       membership_status='inactive'

   return Member(first_name, last_name, membership_id, membership_status)

def serach_member(members) :
    clear_screen()
    print("\nSearch by: \n")
    print("1. Membership ID")
    print("2. First Name")
    print("3. Membership Status\n")

    search_choice= input("Enter your choice: ")

    found_members =[]

    if search_choice == '1':
        search_id= input("Enter the membership ID to search: ")
        for x in members:
            if x.membership_id == search_id:
                found_members.append(x)
                break
    
    elif search_choice == '2':
        first_name= input("Enter the first name to search: ")
        for x in members:
            if x.first_name.lower() == first_name.lower():
                found_members.append(x)
    
    elif search_choice =='3':
        membership_status = input ("Etner the membership status to search (active / inactive): ")
        for x in members:
            if x.membership_status.lower() == membership_status.lower():
                found_members.append(x)

    else:
        print("Sorry,Invalid choice ")

    if found_members:
        clear_screen()
        print("Members found: ")
        for x in found_members:
            x.display_member()
    else:
        print("member not found!")
        time.sleep(2)

members=[]

while True:
    clear_screen()
    print("\n  welcome to Gym membership management \n")
    print("\n  Choose an action: \n") 
    print("1. add new member")
    print("2. Display all members")
    print("3. Search for a member")
    print("3. Exit \n")

    choice = input("Enter your choice: ")

    if choice == '1':
        members.append(create_member())
        print("members added successfully!" )
        time.sleep(2)
    
    elif choice=='2':
        clear_screen()
        if members:
            print ("Displaying all members ....")
            time.sleep (5)
            for i in members:
                i.display_member()
            time.sleep(6)
        else:
            print("sorry, do not find any members to display!")
            time.sleep(2)
        
    elif choice=='3':
        if members:
            serach_member(members)
            time.sleep(5)
        else:
            print("No Member to search...,")
            time.sleep(2)

    elif choice=='4':
        print("Exiting ....")
        time.sleep(5)

    else:
        print("lnvalid choice! Please try again.")
        time.sleep(5)
