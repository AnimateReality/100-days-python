# Playing around with if and else statements
age = int(input("what is yout age?"))
height= int(input("what is your height in cm?"))

if age >= 10:
    if height >= 120:
        print("Welcome aboard, please pay $10 dollars at the entrance")
    else:
        print("sorry you're not tall enough")
else:
    print("sorry you're not old enough yet")
