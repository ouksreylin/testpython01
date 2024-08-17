import random
rock = '''
    ___
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ___
---'   __)__
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    ___
---'   __)__
          ______)
       __________)
      (____)
---.__(___)
'''
choice=[rock,paper,scissors]
print('What is your choice ? Type 0 for Rock, 1 for Paper or 2 forScissors.')
yourchoice=int(input("Your Choice : "))
print(choice[yourchoice])
computerchoice=random.randint(0,2)
print(choice[computerchoice])
print(f"Computer Choice :{computerchoice}")
if yourchoice==0:
    if computerchoice==1:
        print("Computer win")
    elif computerchoice==2:
        print("Your win")
    else:
        print("Draw")
elif yourchoice==1:
    if computerchoice==2:
        print("Computer win")
    elif computerchoice==0:
        print("Your win")
    else:
        print("Draw")
elif yourchoice==2:
    if computerchoice==0:
        print("Computer win")
    elif computerchoice==1:
        print("Your win")
    else:
        print("Draw")
