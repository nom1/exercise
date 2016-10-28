#this calculates BMI depending on your weight and height.
def BMI_calc ():          
    weight_kg = float(raw_input("what is your weight (kg): "))
    height_cm = int(raw_input("what is your height (cm): "))
    weight = weight_kg *  2.2
    height = height_cm  *  0.3937007874
    BMI = (weight/(height*height))*703
    if BMI > 18.5 and BMI < 25:
        print("you are within the ideal range")
    elif BMI > 25:
        print("you are overweight. you should see your doctor.")
    else:
        print("your BMI is {0}.".format(BMI))
        print("you are underweight. you should see your doctor")


BMI_calc()
