print("===== Body Mask Index (BMI) =====")
weight =input("Input your weight in Kg : ")
height = input("Input your height in m: ")
BMI=float(weight)//float(height)**2
#print("Your BMI = "+str(int(BMI)))
print("Your BMI = ",int(BMI))
#print(f'For Weight = {weight} and Height = {height} so Your BMI = {BMI}')
#print("For Weight = {} and Height = {} so Your BMI = {}".format(weight,height,BMI))
#classification=""
if BMI<16 :
    print("Classification is Severe Thinness.")
elif BMI<17 :
    print("Classification is Moderate Thinness.")
elif BMI<18.5 :
    print("Classification is Mild Thinness.")
elif BMI<25 :
    print("Classification is Normal.")
elif BMI<30:
    print("Classification is Overweight.")
elif BMI<35:
    print("Classification is Obese Class I.")
elif BMI<40:
    print("Classification is Obese Class II.")
else:
    print("Classification is Obese Class III.")


#
# print("=====Welcome to the Tip Calculator=====")
# bill=input("What was the total bill ? $")
# tip =input("How much tip would you like to give? 10%, 12%, 15%? %")
# people=input("How many people to split the bill? ")
#
# payfortip=float(bill)*float(tip)/100
# pay=(float(bill)+payfortip)/float(people)
#
# #print("Each Person should pay : $",pay)
# print(f"Each Person should pay : ${pay}")
