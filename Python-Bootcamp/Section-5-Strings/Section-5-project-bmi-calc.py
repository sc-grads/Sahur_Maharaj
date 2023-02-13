# get parameters
weight = float(input('Enter your weight(kg):'))
height = float(input('Enter your height(m): '))
# use formula for cm an kg
BMI_FORMULA = round((weight / height / height) * 10_000, 2)
# print bmi
print(f'Your BMI is: {BMI_FORMULA}')
