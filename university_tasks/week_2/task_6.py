first_number = int(input("Please enter the first whole number: "))
second_number = int(input("Please enter the second whole number: "))
third_number = int(input("Please enter the third whole number: "))

even = 0
odd = 0

if first_number %2 == 0:
    even += 1
else:
    odd += 1

if second_number %2 == 0:
    even += 1
else:
    odd += 1

if third_number %2 == 0:
    even += 1
else:
    odd += 1

print(f"There are {even} even numbers and {odd} odd numbers.")
