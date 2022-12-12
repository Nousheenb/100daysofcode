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


print("Welcome to rock , paper , scissors game")
choices  = [rock , paper , scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(choices[user_choice])

computer_choice = random.randint(0,2)
print("Computer's choice: ")
print(choices[computer_choice])

if (computer_choice == user_choice) :
  print("Draw")

elif (user_choice == 0 and computer_choice == 2 ) or (user_choice == 1 and computer_choice == 0 )or (user_choice == 2 and computer_choice == 1 ) :
  print("You win.")

else:
  print("You Lose.")
