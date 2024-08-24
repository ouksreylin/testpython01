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
def test_fun(colorlist):
    print(f'ID = {id(colorlist)}')
    colorlist.append("Blue")
    print(f'ID after change {id(colorlist)}')
    print(colorlist)

mycolor=["Red","Black"]
test_fun(mycolor)
print(f'ID outside {id(mycolor)}')
print(mycolor)



