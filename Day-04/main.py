import  random
print("ROCK PAPAER SYSTEM GAME")
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
games_image  =[rock, paper, scissors]
user_choice = int(input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("you type an invalid answer")
else:
 print(games_image[user_choice])
computer_choice = random.randint(0,2)
print("computer choice:")
print(games_image[computer_choice])
if user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")

elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("it is a draw")
