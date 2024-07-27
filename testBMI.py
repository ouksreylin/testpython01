# print("===== Body Mask Index (BMI) =====")
# weight =input("Input your weight in Kg : ")
# height = input("Input your height : ")
# BMI=float(weight)//float(height)**2
# #print("Your BMI = "+str(int(BMI)))
# # print("Your BMI = ",int(BMI))
# print(f'For Weight = {weight} and Height = {height} so Your BMI = {BMI}')
# print("For Weight = {} and Height = {} so Your BMI = {}".format(weight,height,BMI))


print("=====Welcome to the Tip Calculator=====")
bill=input("What was the total bill ? $")
tip =input("How much tip would you like to give? 10%, 12%, 15%? %")
people=input("How many people to split the bill? ")

payfortip=float(bill)*float(tip)/100
pay=(float(bill)+payfortip)/float(people)

#print("Each Person should pay : $",pay)
print(f"Each Person should pay : ${pay}")
