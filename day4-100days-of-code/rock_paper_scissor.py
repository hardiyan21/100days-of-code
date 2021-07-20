import random
import inquirer

rock_icon = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_icon = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_icon = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice_list = [rock_icon, paper_icon, scissors_icon]

user_choice = [
    inquirer.List('rps',
    message="Please choose your hero!",
    choices=['rock', 'paper', 'scissors'],)
]
answers = inquirer.prompt(user_choice)
#print(answers['rps'])

if (answers['rps']) == "rock":
    print(rock_icon)
elif (answers['rps']) == "paper":
    print(paper_icon)
else:
    print(scissors_icon)

print("-------------------------------")

computer_choice = random.choice(choice_list)
print(computer_choice)

# if (answers['rps']) == computer_choice:
#     print("You are draw with computer, please try again!")
if (answers['rps'] == 'rock') and (computer_choice == paper_icon):
    print("You are loss!, computer win with paper")
elif (answers['rps'] == 'paper') and (computer_choice == rock_icon):
    print("You are win!, computer loss with rock")
elif (answers['rps'] == 'scissors') and (computer_choice == rock_icon):
    print("You are loss!, computer win with rock")
elif (answers['rps'] == 'rock') and (computer_choice == scissors_icon):
    print("You are win!, computer loss with scissors")
elif (answers['rps'] == 'paper') and (computer_choice == scissors_icon):
    print("You are loss!, computer win with scissors")
elif (answers['rps'] == 'scissors') and (computer_choice == paper_icon):
    print("You are win!, computer loss with paper")
else:
    print("You are draw with computer, please try again!")