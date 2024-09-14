# #14-09-24
# import math
# import myModule
#
# val =math.sqrt(16)
# print(val)
#
# print(myModule.PI)
# myModule.sayhello("John")
#
# import myCal        # import all function in myCal file
# print("Sum:",myCal.sum(10,20))
# print("Average:",myCal.average(10,20))
# print("Power:",myCal.power(10,2))
#
# from myCal import *     # import all function in myCal file
# print("Sum:",sum(10,20))
# print("Average:",average(10,20))
# print("Power:",power(10,2))
#
# from myCal import sum,average       # import some function in myCal file
# print("Sum:",sum(10,20))
# print("Average:",average(10,20))
#
# import myCal as d # rename file from muyCal to d
# print(d.sum(2,4))
# print(d.average(2,4))
# print(d.power(2,4))

from myPackage import *
sayhello("John")
print(sum(2,3))
print(average(2,3))
print(power(2,3))
print(sqrt(100))