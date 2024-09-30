import random

rock_ascii = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_ascii = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_ascii = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock_ascii, paper_ascii, scissors_ascii]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0, len(choices) - 1)
user = "user"
computer = "computer"

winner = "draw"
if user_choice < 0 or user_choice > 2:
    print("You entered invalid number")
elif user_choice == 0:
    if computer_choice == 1:
        winner = computer
    elif computer_choice == 2:
        winner = user
elif user_choice == 1:
    if computer_choice == 0:
        winner = user
    elif computer_choice == 2:
        winner = computer
elif user_choice == 2:
    if computer_choice == 0:
        winner = computer
    elif computer_choice == 1:
        winner = user

print("You chose:")
print(choices[user_choice])
print("Computer chose:")
print(choices[computer_choice])
if winner == user:
    print("You won!")
elif winner == computer:
    print("You lost!")
else:
    print("Draw!")