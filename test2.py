# class Book:
#     title=""
#     author=""
#     pages=0
# my_book=Book()
# my_book.title="origin"
# my_book.author="Dan Brown"
# my_book.pages=542

# print(my_book.title)
# print(my_book.author)
# print (my_book. pages)

# class Book:
#     def __init__(self, title, author, pages):
#        self.title=title
#        self.author=author
#        self.pages=pages

# my_book=Book("origin", "Dan brown", 542)
# third_book=Book("ghaly", "Youssef", 434)

# print (my_book.author)
# print(third_book.title)
# class Profile:
#     def __init__(self, name, email, language):
#         self.name=name
#         self.email=email
#         self.language=language
        
# ghaly=Profile("maka", "ekjkjkjfkjk@gmail.com", "arabic")
# samuel=Profile("sam", "dkjil@gmail.com", "rabic")

# print(ghaly.email)
# print(samuel.email)

# class Task:
#     def __init__ (self, title, description, due_date, status):
#         self.title= title
#         self.description= description
#         self.due_date = due_date
#         self.status= status
#     def display_task(self):
#          print(f"Title: {self.title}" )
#          print (f"Description: {self.description}")
#          print(f"Due Date: {self.due_date}")
#          print(f"Status: {self.status}")

#     def mark_as_complete(self): # to change the task status to complete
#         self.status="complete"


# taskl = Task("Review Syntax" , "Review how to create calss and,.....",9-10-2026, "incomplete")
# taskl.display_task()
# taskl.mark_as_complete()
# taskl.display_task()

# class MoviesList:
#     def __init__(self, Title, Director, Release_Year, Genre):
#         self.Title=Title
#         self.Director=Director
#         self.Release_Year=Release_Year
#         self.Genre=Genre

#     def MOVIES_LIST(self):
#         print(f"____MOVIES LIST____")
#         print(f"Title: {self.Title}")
#         print(f"Director: {self.Director}")
#         print(f"Release_Year: {self.Release_Year}")
#         print(f"Genre: {self.Genre}")

#     def update_director(self,new_director):
#         self.Director=new_director

# List_1=MoviesList("Inception", "Christ serlva", "2010", "Sci_Fi")
# List_2=MoviesList("abcvs", "Cjjhjhj", "2011", "Romantic")
# List_3=MoviesList("dssw", "A7A", "2011", "Romantic")

# List_1.MOVIES_LIST()
# List_2.update_director("jackie chan")
# List_2.MOVIES_LIST()

# class User:
#     def __init__(self, first_name, last_name, email, password, status='inactive'):
#       self.first_name = first_name
#       self.last_name= last_name
#       self.email = email
#       self.password= password
#       self. status= status
     
# def create_user():
#    first_name = input("Enter your first name: ")
#    last_name= input("Enter your last name: ")
#    email = input("Enter your email: ")
#    password = input("Enter your password: ")

#    return User(first_name,last_name,email,password )
       
# userl =create_user()
# print(userl.first_name)

#another example :

# class Recipe:
#     def __init__(self, name, ingriedients, cooking_time, instructions):
#         self.name= name
#         self.ingrediants=ingriedients
#         self.cooking_time= cooking_time
#         self.instructions=instructions

#     def display_receipe(self):
#         print(f"Name: {self.name}")
#         print(f"Ingrediants: {self.ingrediants}")
#         print(f"Cooking Time: {self.cooking_time}")
#         print(f"Instruction: {self.instructions}")
#         print ("_" *20)

# def create_recipe():
#     name=input("Enter receipe name : ")
#     ingrediants=input("Enter ingrediants (comma-seprated) : ")
#     cooking_time=input("Enter cooking time: ")
#     instructions=input("Enter cooking instructions : ")
#     return Recipe(name, ingrediants,cooking_time, instructions)

# print("Welcome to Recipe Collection \n")
# my_recipe=create_recipe()
# print("Recipe added successfully! \n")
# my_recipe.display_receipe()

#another
# import os
# import time

# def clear_screen():
#     os.system('cls' if os.name  == 'nt' else 'clear')
# class User:
#    def __init__ (self, first_name, last_name, email, password, status='inactive') :
#       self.first_name = first_name
#       self.last_name =last_name
#       self.email = email
#       self.password =password
#       self.status =status

#    def display_user(self) : 
#         print(f"First name: {self.first_name}")
#         print(f"Last name: {self.last_name}")
#         print(f"Email: {self.email}")
#         print(f"Status: {self.status}")
#         print ("_" *20)

# def create_user():
#    first_name = input("Enter your first name: ")
#    last_name= input("Enter your last name: ")
#    email = input("Enter your email: ")
#    password = input("Enter your password: ")

#    return User(first_name,last_name,email,password )

# new_users=[]

# while True:
#     print("\n  welcome to user management \n")
#     print("\n  Choose an action: \n") 
#     print("1. add new user")
#     print("2. Display all users")
#     print("3. Exit \n")

#     choice = input("Enter your choice:")

#     if choice == '1':
#         new_users.append(create_user())
#         print("User addess successfully!" )
#         time.sleep(2)
    
#     elif choice=='2':
#         clear_screen()
#         if new_users:
#             print ("Displaying all new users ....")
#             time.sleep (1)
#             for i in new_users:
#                 i.display_user()
#             time.sleep(2)
#         else:
#             print("sorry, do not find any user to display!")
#             time.sleep(2)
#     elif choice=='3':
#         print("Exiting ....")
#         break

#     else:
#         print("lnvalid choice! Please try again.")


##############
#   another

# import os
# import time

# def clear_screen():
#     os.system('cls' if os.name  == 'nt' else 'clear')
# class Member:
   
#    def __init__ (self, first_name, last_name, membership_id, membership_status='inactive') :
#       self.first_name = first_name
#       self.last_name =last_name
#       self.membership_id=membership_id
#       self.membership_status=membership_status
    

#    def display_member(self):
#         print(f"First name: {self.first_name}")
#         print(f"Last name: {self.last_name}")
#         print(f"Membership_id: {self.membership_id}")
#         print(f"Membership_status: {self.membership_status}")
#         print ("_" *20)

# def create_member():
#    first_name = input("Enter your first name: ")
#    last_name= input("Enter your last name: ")
#    membership_id=input("Enter your membership_id: ")
#    membership_status= input("Enter your membership status or press Enter: ")
#    if not membership_status:
#        membership_status='inactive'

#    return Member(first_name, last_name, membership_id, membership_status)

# def serach_member(members) :
#     clear_screen()
#     print("\nSearch by: \n")
#     print("1. Membership ID")
#     print("2. First Name")
#     print("3. Membership Status\n")

#     search_choice= input("Enter your choice: ")

#     found_members =[]

#     if search_choice == '1':
#         search_id= input("Enter the membership ID to search: ")
#         for x in members:
#             if x.membership_id == search_id:
#                 found_members.append(x)
#                 break
    
#     elif search_choice == '2':
#         first_name= input("Enter the first name to search: ")
#         for x in members:
#             if x.first_name.lower() == first_name.lower():
#                 found_members.append(x)
    
#     elif search_choice =='3':
#         membership_status = input ("Etner the membership status to search (active / inactive): ")
#         for x in members:
#             if x.membership_status.lower() == membership_status.lower():
#                 found_members.append(x)

#     else:
#         print("Sorry,Invalid choice ")

#     if found_members:
#         clear_screen()
#         print("Members found: ")
#         for x in found_members:
#             x.display_member()
#     else:
#         print("member not found!")
#         time.sleep(2)

# members=[]

# while True:
#     clear_screen()
#     print("\n  welcome to Gym membership management \n")
#     print("\n  Choose an action: \n") 
#     print("1. add new member")
#     print("2. Display all members")
#     print("3. Search for a member")
#     print("3. Exit \n")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         members.append(create_member())
#         print("members added successfully!" )
#         time.sleep(2)
    
#     elif choice=='2':
#         clear_screen()
#         if members:
#             print ("Displaying all members ....")
#             time.sleep (5)
#             for i in members:
#                 i.display_member()
#             time.sleep(6)
#         else:
#             print("sorry, do not find any members to display!")
#             time.sleep(2)
        
#     elif choice=='3':
#         if members:
#             serach_member(members)
#             time.sleep(5)
#         else:
#             print("No Member to search...,")
#             time.sleep(2)

#     elif choice=='4':
#         print("Exiting ....")
#         time.sleep(5)

#     else:
#         print("lnvalid choice! Please try again.")
#         time.sleep(5)


#another 
# from turtle import Turtle, Screen

# sam=Turtle()
# sam.shape("turtle")
# sam.forward (100)
# sam.left (90)
# sam.forward(200)

# window = Screen()

# window.exitonclick()

#######

# from turtle import Turtle, Screen

# sam=Turtle()
# sam.shape("turtle")

# for _ in range(4):
#     sam.forward(100)
#     sam.left(110)
    
# window = Screen()

# window.exitonclick()

##############

# from turtle import Turtle, Screen

# sam=Turtle()
# sam.shape("turtle")
# sam.color("mediumaquamarine")

# for _ in range(360):
#     sam.forward(1)
#     sam.left(1)
    
# window = Screen()

# window.exitonclick()

###############
# from turtle import Turtle, Screen

# sam=Turtle()
# sam.shape("turtle") # turtle, square, triangle, circle, classic
# sam.color("mediumaquamarine")
# sam.speed("fastest") # slow, normal, fast, fastest

# sam.penup()
# sam.forward(100)
# sam.pendown()
# sam.pendown()
# sam.pensize(5)
# sam.forward(100)
    
# window = Screen()
# window.exitonclick()

#######################
# from turtle import Turtle, Screen

# sam=Turtle()
# sam.shape("turtle") # turtle, square, triangle, circle, classic
# sam.color("mediumaquamarine")

# def draw_a_square():
#     for _ in range(4):
#         sam.forward(100)
#         sam.left(90)

# draw_a_square()
    
# window = Screen()
# window.exitonclick()

########################
# from turtle import Turtle, Screen
# import random

# sam=Turtle()
# window = Screen()

# list_of_colors=["mediumaquamarine", "blue", "red", "yellow", "green", "orange", "purple", "pink"]
# list_of_shapes=["turtle", "square", "triangle", "circle", "classic"]
# list_of_speeds=["slow", "normal", "fast", "fastest"]
# list_of_pen_sizes=[1, 2, 3, 4, 5]

# sam.speed("slowest")


# def draw_a_square():
#     for _ in range(4):
#         sam.color(random.choice(list_of_colors))
#         sam.pensize(random.choice(list_of_pen_sizes))   
#         sam.shape(random.choice(list_of_shapes))
#         sam.forward(100)
#         sam.left(90)

# draw_a_square()
    
# window.exitonclick()

######################
# from turtle import Turtle, Screen
# import random

# window = Screen()
# window.bgcolor("black")
# window.setup(width=800, height=600)


# list_of_colors=["mediumaquamarine", "blue", "red", "yellow", "green", "orange", "purple", "pink"]
# list_of_shapes=["turtle", "square", "triangle", "circle", "classic"]
# list_of_speeds=["slow", "normal", "fast", "fastest"]
# list_of_pen_sizes=[1, 2, 3, 4, 5]

# sam=Turtle()
# sam.shape("turtle") # turtle, square, triangle, circle, classic
# sam.color("white")
# sam.pensize(5)
# sam.speed("fast") # slow, normal, fast, fastest

# tom=Turtle()
# tom.shape("turtle")
# tom.color("red")
# tom.pensize(5)
# tom.speed("fast")

# my_angles=[0, 90, 180, 270]  #tuple immutable
# my_distances=[50, 100, 150, 200]
# loop_count=[5,10,15,20]


# def draw_random(turtle_name):
#     for _ in range(random.choice(loop_count)):
#         turtle_name.forward(random.choice(my_distances))
#         turtle_name.left(random.choice(my_angles))

# draw_random(sam)
# draw_random(tom)

# window.exitonclick()

######################
# from turtle import Turtle, Screen

# window = Screen()
# window.bgcolor("black")
# window.setup(width=1000, height=1000)

# sam=Turtle()
# sam.shape("turtle") # turtle, square, triangle, circle, classic
# sam.color("white")
# sam.pensize(5)
# sam.speed("fast") # slow, normal, fast, fastest
# def draw_circle():
#     sam.penup() 
#     sam.goto(-300,-300)  # Move to the starting position
#     sam.pendown()
#     for _ in range(10): # Draw 10 circles to complete a full rotation
#         sam.circle(50)  # Draw a circle with radius 50
#         sam.left(360/10)  # Turn left by 36 degrees

# def draw_square():
#     sam.penup()
#     sam.goto(0, 0)  # Move to the starting position
#     sam.pendown()
#     for _ in range(10): # Draw 10 squares to complete a full rotation
#         for _ in range(4):  # Draw a square
#             sam.forward(80)  # Move forward by 80 units
#             sam.left(90)  # Turn left by 90 degrees
#         sam.left(360/10)  # Turn left by 36 degrees

# def draw_triangle():
#     sam.penup()
#     sam.goto(300,300)  # Move to the starting position
#     sam.pendown()
#     for _ in range(10): # Draw 10 triangles to complete a full rotation
#         for _ in range(3):  # Draw a triangle
#             sam.forward(100)  # #ove forward by 100 units
#             sam.left(120)  # Turn left by 120 degrees
#         sam.left(360/10)  # Turn left by 36 degrees

# draw_circle()
# draw_square()
# draw_triangle()

# window.exitonclick()

######################
from turtle import Turtle, Screen
window = Screen()

sam=Turtle()
user_name= window.textinput("User Name", "Please enter your name:")
sam.hideturtle()
sam.write(f"Hello, {user_name}!", align="center", font=("Arial", 20, "normal")) 


window.exitonclick()
