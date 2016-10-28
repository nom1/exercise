def temperature():

    print("press C to convert from farenheit to celsius")
    print("press F to convert from celsius to farenheit")
    choice = raw_input()
    print("your choice " + choice)
    if choice == "c":
        F = int(raw_input("please enter the temperature in farenheit: "))
        sum1 = (F-32)*5/9
        print(sum1)
    else:
        C = int(raw_input("please enter the temperature in celsius: "))
        sum2 = (C*9/5)+32
        print(sum2)
  

temperature()
