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

game_choices = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 Scissors.\n"))

computer_choice = random.randint(0, 2)

if player_choice >= 3 or player_choice < 0:
    print("Type a valid number!")
else:
    print(f"You chose:\n{game_choices[player_choice]}\nComputer chose:\n{game_choices[computer_choice]}")

    if player_choice == computer_choice:
        print("You tied")
    elif player_choice == 0 and computer_choice == 1:
        print("You lose")
    elif player_choice == 0 and computer_choice == 2:
        print("You won!")
    elif player_choice == 1 and computer_choice == 0:
        print("You won!")
    elif player_choice == 1 and computer_choice == 2:
        print("You lose")
    elif player_choice == 2 and computer_choice == 0:
        print("You lose")
    elif player_choice == 2 and computer_choice == 1:
        print("You won!")

    
    