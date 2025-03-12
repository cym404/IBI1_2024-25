weight=float(input("your weight?(kg)")) #get user's weight
height=float(input("your height?(m)")) #get user's height
bmi=weight/(height**2) #calculate bmi
if bmi<18.5:
    print("your bmi is",bmi,"underweight") #print underweight if bmi is lower than 18.5
elif bmi<=30:
    print("your bmi is",bmi,"normal weight") #print normal weight if bmi is higher than 18.5 but lower than 30
else:
    print("your bmi is",bmi,"obese") #print obese if bmi is higher than 30
