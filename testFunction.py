# #24.08.2024
#
# #non return type function
# def greeting(name):
#     print("Hello",name)
#
#
# greeting("John")
#
# #return type function
# def get_total(val1,val2):
#     total=val1+val2
#     return total
#
# #print(get_total(4,5))
# total=get_total(4,5)
# print(total)

# Test pass by value
# def test_fun(val):
#     print(f'ID = {id(val)}')
#     val=val+1
#     print(f'ID after change {id(val)}')
#     print(val)
#
# amount=5
# test_fun(amount)
# print(f'ID outside {id(amount)}')
# print(amount)

#Test pass by reference
# def test_fun(colorlist):
#     print(f'ID = {id(colorlist)}')
#     colorlist.append("Blue")
#     print(f'ID after change {id(colorlist)}')
#     print(colorlist)
#
# mycolor=["Red","Black"]
# test_fun(mycolor)
# print(f'ID outside {id(mycolor)}')
# print(mycolor)


#31.08.2024

# #all variable before / is set value by position (can not use name of variable Ex: 1000(true) not amount=100(false))
# def interest(amt,rate,/):
#     return amt*rate/100
#
# interest_amt=interest(10000,1)
# print(f'Interest Amount {interest_amt}')


# def my_fun(x,y,z):  # all variable can have name of variable and have not name of variable(Ex 100 and a=100 (true all))
#     print(x,y,z)
#
# my_fun(2,3,4)

# #all variable after * is set value by keyword (Ex: x=3 (true) 3(false))
# def my_fun(x,y,*,z):
#     print(x,y,z)
#
# my_fun(2,3,z=5)

# def show_info(name,city="BMC"): # city="BMC" it call default argument
#     print(name,city)
#
# show_info("Dara","BTB")


# def fcn(nums,numberList=[]): #mutable : not overide old values
#     numberList.append(nums+1)
#     print(numberList)
#
# fcn(5)
# fcn(10)
# fcn(15)

# def greeting(message,*name): #variable-lenght : set as string do not have keyword
#     for val in name:
#         print(f'{message} {val}')
#
#
# greeting("Good morning","Dara","Thida","John","Cheath")

# lambda function
# sum=lambda val1,val2:val1+val2 #lambda function: write it only one line
# print(sum(2,3))


def myfunction(a:int,b:int)->int:    # show datatype int annotation
    return a+b

print(myfunction("as","s"))
print(myfunction.__annotations__)


def myfunction2(a:"Should int",b:"Should int")->int:    # show "Should int "in annotation
    return a+b

print(myfunction2.__annotations__)