import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = input("Choose 'rock', 'paper' or 'scissors by typing '0', '1', or '2'\n")
images = [rock, paper, scissors]
if int(choice) > 3 or int(choice) <0:
    print("You picked an invalid number")
else:
    
    your_choice = images[int(choice)]
    # options = ['rock', 'paper', 'scissors']
    ai_choice = random.choice(images)
    # Game messages
    draw = "Unfortunately its a draw. Want to play again?"
    win = "Congratulations! You win."
    lose = "Sorry, you lost."

    print("You chose " + images[int(choice)] + " and the Computer chose " + ai_choice)

    if your_choice == ai_choice:
        print(draw) 
    elif your_choice == rock:
        if ai_choice == scissors:
            print(win)
        if ai_choice == paper:
            print(lose)
    elif your_choice == paper:
        if ai_choice == rock:
            print(win)
        if ai_choice == scissors:
            print(lose)
    elif your_choice == scissors:
        if ai_choice == paper:
            print(win)
        if ai_choice == rock:
            print(lose)
    else:
        print("Check your input, please only type the numbers 0, 1 or 2")
        print(your_choice)
        print(ai_choice)
