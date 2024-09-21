# # 14-08-24
# my_set={1,2,3,4,5,5}
# print(my_set)
#
# my_set2=set([1,2,3,3,4])
# print(my_set2)
# for val in my_set2:
#     print(val)
#
#
# my_list=[val for val in my_set2]
# print(my_list)
#
# my_list=[val**2 for val in my_set2 if val<4]
# print(my_list)


    #21-08-24
my_set={1,2,3,3,5,8,7}
print(my_set)
print(4 in my_set)
my_set2={3,5,6,9}
print(my_set2.issubset(my_set))

my_set.add(10)
print(my_set)
my_set.update(my_set2)
print(my_set)


s3=set("hello")
s4=set("hi")
s3.update(s4)
print(s3)


#union() like update() but union have new variable to put all value (set1 and set2)
s1={"PHP","C#","Python"}
s2={"C++","Python","VB"}

#s3=s1.union(s2)
s3=s1 | s2
print(s3)

#comprehension
number_list={1,2,3,4}
new_set={d**2 for d in number_list if d<4}
print(new_set)








