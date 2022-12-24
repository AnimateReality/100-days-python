print("Welcome to the love calculator")
name1= input("What is yout name? \n")
name2= input("What is their name? \n")

low_name1 = name1.lower()
low_name2 = name2.lower()

true = 0
true += low_name1.count("t") + low_name1.count("r") + low_name1.count("u") + low_name1.count("e")
true += low_name2.count("t") + low_name2.count("r") + low_name2.count("u") + low_name2.count("e")
love = 0
love += low_name1.count("l") + low_name1.count("o") + low_name1.count("v") + low_name1.count("e")
love += low_name2.count("l") + low_name2.count("o") + low_name2.count("v") + low_name2.count("e")
combining = str(true) + str(love)
true_love = int(combining)

if true_love < 10 or true_love > 90:
    print("Your score is " + combining + " you go together like coke and mentos")
elif true_love > 40 and true_love <50:  
    print("Your score is " + combining + " you are alright together")
else:
    print("Your score is " + combining)


