print("Welcome to the Python Pizza Deliveries")
size = input("What size pizza do you want?")
add_pepperoni = input("Do you want pepperoni")
extra_cheese = input("Do you want extra cheese?")
total = 0
if size == "L":
    total = 25
if add_pepperoni == "Y":
    total += 2
if extra_cheese == "Y":
    total += 3
if size == "M":
    total = 20
if add_pepperoni == "Y":
    total += 2
if extra_cheese == "Y":
    total += 3
if size == "S":
    total = 15
if add_pepperoni == "Y":
    total += 2
if extra_cheese == "Y":
    total += 3

# work in progress right now I read the brief wrong

print(total)