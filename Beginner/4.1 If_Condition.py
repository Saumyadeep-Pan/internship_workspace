try:
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))

    bmi = weight / (height**2)

    if bmi >= 30:
        print('BMI result: "Obesity"')
    elif 25 <= bmi < 30:
        print('BMI result: "Overweight"')
    elif 18.5 <= bmi < 25:
        print('BMI result: "Normal"')
    else:
        print('BMI result: "Underweight"')

except ValueError:
    print("Input error: Please make sure to input numbers only.")
except ZeroDivisionError:
    print("Math error: Height cannot be zero.")
