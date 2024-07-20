            #20-07-2024
# test datatype
str_text = "Hello World"
print(str_text)  # print all
print(str_text[2:5]) # print from index 2 to 5
print(str_text[2:])  # print from index 2 to all index after 2
print(str_text*3)    # print all 3times
print(str_text+"From BBU")   # print all and add string

# test number
a=1_000_000
print(a)    # print a
print(type(a))  # print type of a

b=13.04
print(b)
print(type(b))

# test error
val1=int("10")
val2=int("20")
total=val1+val2
print("Total = "+ str(total))
print(len(str(total)))  # count number