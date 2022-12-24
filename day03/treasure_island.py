print('''
                         ____
                  /^\   / -- )
                 / | \ (____/
                / | | \ / /
               /_|_|_|_/ /
                |     / /
 __    __    __ |    / /__    __    __
[  ]__[  ]__[  ].   / /[  ]__[  ]__[  ]
|__            ____/ /___           __|
   |          / .------  )         |
   |         / /        /          |  SheDragon
   |        / /        /           |
~~~~~~~~~~~~-----------~~~~~~~~ldb~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
print("Welcome to Treasure Island")
print("You're mission is ot find the hidden treasure")

choice1 = input('You\'re at a cross road Where do you want to go? Type "left" or "right"').lower()
if choice1 == "left":
    choice2 = input('Would you like to "swim" across the lake or "wait"?').lower()  
    if choice2 == "wait":
        print("You arrive at and intersection with 3 doors. Red, Blue and Yellow.")
        choice3 = input('Type to choose which: "red", "blue" or "yellow"?').lower()
        if choice3 == "blue":
            print("You got burned by fire. \nGame Over")
        elif choice3 == "blue":
                print("You got eaten by beasts. \nGame Over")
        elif choice3 == "yellow":
                print("You win!")
        else:
            print("Game Over.")
    else:
        print("You got attacked by trout.\n Game Over.")
else:
    print("You fell into a hole.\n Game Over.")

# treasure island game based off flow chart from https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload