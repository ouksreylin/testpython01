print("Welcome to the rollercoaster")
height=int(input("What is your height in cm ?"))
bill=0
if height>=120 :
    print("Ok You can ride rollercoaster.")
    age=int(input("How old are you?"))
    if age<12 :
        bill=5
    elif age<18 :
        bill=7
    else:
        bill=12

    photo=input("Do you want photo? Y or N :")
    if photo.upper()=="Y" :
        bill+=3

    print(f'Your total Pay : {bill} $')

else :
    print("Sorry , you are shorter.")