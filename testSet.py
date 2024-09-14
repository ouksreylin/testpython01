# 14-08-24
my_set={1,2,3,4,5,5}
print(my_set)

my_set2=set([1,2,3,3,4])
print(my_set2)
for val in my_set2:
    print(val)


my_list=[val for val in my_set2]
print(my_list)

my_list=[val**2 for val in my_set2 if val<4]
print(my_list)