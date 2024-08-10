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

            # for in loop (range)
# for count in range(6):
#     print(f'Data {count}')



    #10-08-2024

# for val in range(10):
#     print(val)

# for val in range(2,10):
#     print(val)

# for val in range(2,10,2):
#     print(val)


        # loop with string
    # ('''   ''' : can write multi line.)
# message='''
#     hello from BBU
# '''
# for cha in message:
#     if cha not in 'aeiouAEIOU':
#         print(cha,end="")


#         #loop in tuples
# numbers=(3,4,5,1)
# total=0
# for num in numbers:
#     total+=num
#
#
# print(f'Total = {total}')

            #loop in list
# numbers=[23,45,64,78,13,48]
# for d in numbers:
#     if d%2==0:
#         print(d)

# lenNum=len(numbers)
# for ind in range(lenNum):
#     print(numbers[ind])



            #loop with dictionary
numbers={10:"Ten",20:"Twenty",30:"Thirty"}
#for val in numbers:     #print only key
#   print(val)

# for val in numbers.keys():     #print only key
#     print(numbers[val])         #print value of key

# for val in numbers.items():     #print key and value
#     print(val)

# for k,val in numbers.items():     #print key and value
#     print(f'Key ={k} val = {val}')


        #practice : sum even number
# print("Sum even number")
# num =int(input("Input Number : "))
# total=0
# for n in range(num+1):
#     if n%2==0:
#         total+=n
#
#
# print(f'Total = {total}')



        #while loop statement
# count =0
# while count <5 :
#     count+=1
#     print("Iteration no. {}".format(count))
#
# print("End of while loop")


            # isnumberic()
# val1="0"
# #print(val1.isnumeric())
# while val1.isnumeric()==True:
#     if(val1.isnumeric()==True):
#         print(f"Your input {val1}")
#     val1 = "Test"
#
# print("End loop")
