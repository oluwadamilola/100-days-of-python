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
user_choice = input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors.")
computer_choice = random.randint(0,2)
print(f"computer choice {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice > user_choice:
    print("you lose")
