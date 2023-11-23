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

computer = random.choice(['rock', 'paper', 'scissors'])
print (computer)
player = input("Enter 0 for 'Rock', 1 for 'Paper' and 2 for 'Scissors' \n")

if player == '0':
  player_selection = rock
elif player == '1':
  player_selection = paper
elif player == '2':
  player_selection = scissors

if computer == 'rock':
  computer_selection = rock
elif computer == 'paper':
  computer_selection = paper
elif computer == 'scissors':
  computer_selection = scissors
  
print("\n\n You \n" + player_selection)
print ("\n Computer \n" + computer_selection)
if player_selection == computer_selection:
  print("It's a tie")
elif player_selection == rock and computer_selection == scissors:
  print("You win!")
elif player_selection == scissors and computer_selection == paper:
  print("You win!")
elif player_selection == paper and computer_selection == rock:
  print("You win!")
else:
  print("You lose")