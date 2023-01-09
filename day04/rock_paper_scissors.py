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
choice = input("Choose 'rock', 'paper' or 'scissors'\n")

options = ['rock', 'paper', 'scissors']
ai_choice = random.choice(options)

# Game messages
draw = "Unfortunately its a draw. Want to play again?"
win = "Congratulations! You win."
lose = "Sorry, you lost."
print("You chose " + choice + " and the Computer chose " + ai_choice)

if choice == ai_choice:
    print(draw) 
elif choice == 'rock':
    if ai_choice == 'scissors':
        print(win)
    if ai_choice == 'paper':
        print(lose)
elif choice == 'paper':
    if ai_choice == 'rock':
        print(win)
    if ai_choice == 'scissors':
        print(lose)
elif choice == 'scissors':
    if ai_choice == 'paper':
        print(win)
    if ai_choice == 'rock':
        print(lose)

