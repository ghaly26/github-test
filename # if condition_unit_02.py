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
# if condition with nested if
#========================================================#