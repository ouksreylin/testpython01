#list=['abcd',56,'ef','73']

# print(list[0]) #print index 0
# print(list[2]) #prit index 2
# print(list[-1]) #print index -1(count from end element to beginning element (count from -1 not 0))
#
# list.append(100)    #add value(one data) to list
# print(list)
# list.extend([12,32]) #add list to list (add new list after old list)
# print(list)
#
# print(list[2:5]) # print from index 2 (5indexs from index 1)
# print(list[2:-3]) #print from index 2 and end before index -3
#
# print(list[2:]) #print from index 2 to all element in list
# print(list[2:]*2) #print list two times from index 2
#
# print(list+list)    #print list sum list
#
# del list[2] # delete index 2
# print(list)
# del list[0:3]   #delete from index 0 to index 3 (list[startindex,number_delete])
# print(list)
# del list[:]
# print(list) #delete all data in list
# list.clear()
# print(list) #clear all data in list

# fruits=['orange','apple','pear','banana','kiwi','apple','banana']
# count_f=fruits.count('apple') # count same value in list
# print(count_f)
# fruits.reverse() # reverse values in list
# print(fruits)
# fruits.sort() # sort values in list from a-z
# print(fruits)
#

# **tuple() same as list[] but have same different :
# 1. tuple use () but list use []
# 2. all values in tuple() can not update add edit delete
#    all values in list[] can update add edit delete


# # range
# # start from 0 to 4 (range(stop))
# for val in range(5):
#     print(val)
#
# # start from 5 to 9 (range(start,stop))
# for val in range(5,10):
#     print(val)
#
# # start from 5 to 9 increase 2 (range(start,stop,step))
# for val in range(5,10,2):
#     print(val)
#
# # use pass when it has not statement or body in for loop
# for _ in range(5):
#     pass


#**** bytes data type
#byte is from 0-255
b1=bytes([65,66,67,68,69])
print(b1)

#print values have data type as byte
b2=b'hello'
print(b2)

#binary number (2)
print(bin(20))

#octal number (8)
print(oct(20))


