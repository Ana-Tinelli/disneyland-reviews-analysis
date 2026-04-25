name = (input("What's is your name? "))
age = (int(input("How old are you? ")))
weight = (float(input("What is your weight - KG? ")))
high = (float(input("How tall are you - meters? ")))

bmi = ((weight) / (high * high))

print(f"You BMI is: {bmi:.2f}")