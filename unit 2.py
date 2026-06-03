#python unit 2
str_length=input("Please type Length : \n")
str_width=input("Please type width: \n")
str_price=input("how much for 1 meter? : \n")

length=float(str_length)
width=float(str_width)
cost=float(str_price)

area=length*width
str_area=str(area)

print("The total area is: " + str_area )
total_cost=area * cost
str_total_cost=str(total_cost)

print("give the guy:$ " + str_total_cost)