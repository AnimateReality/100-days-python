print("Welcome to the Python Pizza Deliveries")
size = input("What size pizza do you want?")
add_pepperoni = input("Do you want pepperoni")
extra_cheese = input("Do you want extra cheese?")
total = 0
if size == "L":
    total = 25
elif size == "M":
    total = 20
elif size == "S":
    total = 15

if add_pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3

if extra_cheese == "Y":
    total += 1


print(total)

# The program: 
# Small Pizza: 15
# Medium Pizza: 20
# Large Pizza: 25

# Pepperoni for small: +2
# Pepperoni for medium or large: +3

# Extra cheese for any size pizza: +1