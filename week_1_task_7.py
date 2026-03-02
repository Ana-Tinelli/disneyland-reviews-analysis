name = input('What is your name? ')
age = int(input('How old are you (in years)? '))
height = float(input('How tall are you (in meters)? ' ))
weight = float(input('How much do you weigh (in kilograms)? '))

bmi = weight / (height * height)

print(f'Your age is {age} years old and your bmi is {bmi:.2f}.')


