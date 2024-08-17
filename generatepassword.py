#pratice generate password
import random
import string

print("         Welcome to Password Generator")
letters = int(input("How many letters would you like in your password?"))
symbols = int(input("How many symbols would you like?"))
nums = int(input("How many numbers would you like?"))

#=== Get all String , symbol, number
mystring = string.ascii_lowercase  # function to show a-z as lowercase
mysymbol = string.punctuation  # function to show all symbols
mynumber = string.digits  # function to show number

    #way 1
tmpPassword = []
tmpPassword += random.choices(mystring, k=letters)
tmpPassword += random.choices(mysymbol, k=symbols)
tmpPassword += random.choices(mynumber, k=nums)
random.shuffle(tmpPassword)
tmpPassword="".join(tmpPassword)

print("---------------------------------------------------")
print(f'Your Password Generator : {tmpPassword}')


    #way 2
#tmpPassword=""
# loop pick value
# for d in range(letters):
#     tmpPassword+=random.choice(mystring)        # function for random variable mystring (array)
#
# for d in range(symbols):
#     tmpPassword += random.choice(mysymbol)  # function for random variable mysymbol (array)
#
# for d in range(nums):
#     tmpPassword += random.choice(mynumber)  # function for random variable mynumber (array)

# convert String to list
# tmpPassword = list(tmpPassword)  # convert tmpPassword to list [tmpPassword]
#
# # shuffle list
# random.shuffle(tmpPassword)  # mix tmpPassword [d5*f3%] only List
#
# # convert list to String
# tmpPassword = ''.join(tmpPassword)  #function join to join with empty string ''
#
# print("---------------------------------------------------")
# print(f'Your Password Generator : {tmpPassword}')
