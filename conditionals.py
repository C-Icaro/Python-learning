is_raining = True
is_cold = True
print("Good Morning!")
if is_raining and is_cold: 
    print("Bring umbrella and jacket!")
elif is_raining and not(is_cold):
    print("Bring umbrella!")
elif not(is_raining) and is_cold:
    print("Bring jacket!")
else:
    print("Umbrella optional!")



#Exercise:

print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))
operator = input("Wich operator? Add, Sub, Mult or Div").lower()

if operator == "add":
    result = num_1 + num_2
    print(f"The sum is: {result}")
elif operator == "sub":
    result = num_1 - num_2
    print(f"The sub is: {result}")
elif operator == "mult":
    result = num_1 * num_2
    print(f"The mult is: {result}")
elif operator == "div":
    result = num_1 / num_2
    print(f"The div is: {result}")
else:
    print("Choose a valid operator")


#Exercise:


def num_days(month):
    days = 31
    if month in {'apr','jun','sep','nov'}:
    #if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in',month,'is',days)
    

num_days('jan')
# optimize/shorten the code in the function
# try to reduce the number of conditionals 
