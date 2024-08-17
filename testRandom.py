    # 17.08.2024
import random

# print(random.randint(2,50)) # random between 2 and 50
print(random.randint(0,2)) # random between 2 and 50
# print(random.random()) # random between 0 and 1 (as float (0.022346876))
# print(random.random()*5) # random between 0 and 5 (as float) (Ex : *100 : random 0 to 100)

        # practice1
# guess=["Heads","Tails"]
# choose=random.randint(0,1)
#print(guess[choose])

choose=random.randint(0,1)
if choose==0:
    print("Heads")
else:
    print("Tails")
