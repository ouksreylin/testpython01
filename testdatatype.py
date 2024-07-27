            #20-07-2024
# # test datatype
# str_text = "Hello World"
# print(str_text)  # print all
# print(str_text[2:5]) # print from index 2 to 5
# print(str_text[2:])  # print from index 2 to all index after 2
# print(str_text*3)    # print all 3times
# print(str_text+"From BBU")   # print all and add string
#
# # test number
# a=1_000_000
# print(a)    # print a
# print(type(a))  # print type of a
#
# b=13.04
# print(b)
# print(type(b))
#
# # test error
# val1=int("10")
# val2=int("20")
# total=val1+val2
# print("Total = "+ str(total))
# print(len(str(total)))  # count number

                #27-07-2024
#Boolean (empty=False , have values=True)
# a=True
# print(bool(a))
# a=0.0
# print(bool(a))
# a=1.0
# print(bool(a))
# a=5
# b=10
# print(bool(a==b))
# a=None
# print(bool(a))
# a=()
# print(bool(a))
# a={}
# print(bool(a))
# a="ABC"
# print(bool(a))
# a=5
# print(bool(a))
# a=-5
# print(bool(a))
#             #practice
# number=input("Input two digit number = ")
# val1=int(number[0])
# val2=int(number[1])
# total=val1+val2
# print("Result = "+str(total))

# val=5
# print(val>3 and val<10)
# print(val>3 or val<4)
#
# x=10
# y=20
# z=0
# print("X and Y : ", x and y)
# print("X or Y : ", x or y)
# print("X and Z : ", x and z)
# print("Z or X : ", z or x)
# print("Y or Z : ", y or z)

#
# a="Hello"
# b=tuple()
# print("a and b : ",a and b)
# print("a or b : ",a or b)
#
# x=[1,2,3]
# y=[10,20,30]
# print("x and y : ",x and y)     # result is value at the end
# print("x or y : ",x or y)   # result is value at the beginning

            #identity operator
a=[1,2,3,4]
b=[1,2,3,4]
c=a
print("a is b : ",a is b)   # check identity (not the same value)
print("a is c : ",a is c)

