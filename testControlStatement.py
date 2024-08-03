# mark=float(input("Your Total Mark = \n"))
# result=""
# if mark>=90 :
#     result="A"
# elif mark>=80 :
#     result="B"
# elif mark>=70 :
#     result="C"
# elif mark>=60 :
#     result="D"
# elif mark>=50 :
#     result="E"
# else :
#     result="F"
#
# print(f'Your Grade is {result}')
#


        #match case
# def check_day(val):
#     output=""
#     match val:
#         case 0:
#             output="Monday"
#         case 1:
#             output="Tuesday"
#         case 2:
#             output="Wednesday"
#         case 3:
#             output="Thursday"
#         case 4:
#             output="Friday"
#         case 5:
#             output="Saturday"
#         case 6:
#             output="Sunday"
#         case _:  # default case
#             output="Wrong Type"
#     print(f'Day is {output}.')
#
#
# check_day(2)
# check_day(3)


            # combine in match case
# def access(user):
#     match user :
#         case 'admin' | 'manager' : return "Full access"
#         case 'teller' : return "Limit access"
#         case _: return "No access"
#
#
# print(access('teller'))
# data=access("admin")
# print(data)




#             #list in match case
# def greeting(detail):
#     match detail:
#         case [time,name]:
#             print(f'Good {time} {name}')
#         case [time,*name]:  # *name is list of name
#             for data in name:
#                 print(f'Good {time} {data}')
#         case _:
#             print("Wrong Type")
#
#
# greeting(["Morning","John","David"])





#             #if statement in match case
# def inte(detail):
#     match detail:
#         case [amount,duration] if amount<10000:
#             return amount*0.02*10000
#         case [amount,duration] if amount>=10000:
#             return amount*0.03*duration
#
#
# print(inte([20000,10]))




#             # loop statement
# words=["one","two","three"]
# for d in words:
#     print(f'Number {d}')
#


#             # while loop
# i=1
# while i<6:
#     print(f'Number {i}')
#     i+=1
#

            # for in range
for count in range(6):
    print(f'Data {count}')
