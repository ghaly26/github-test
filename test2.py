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
