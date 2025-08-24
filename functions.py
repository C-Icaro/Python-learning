#basics:

def greeting(name,age=28):
    print("Hello " + name + ", you are " + str(age) + "!")
    print(f"Hello {name}, you are {age}!")

name = input("Enter your name: ")    
greeting(name,32)
greeting("Judith")


#Functions exercise:
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 

def greeting(name, age=28, color="red"):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
    print('Hello '  +  name.title() + ', you will be ' + str(age+1) +' years old next birthday!')
    print(f'Hello {name.title()}, you will be {age+1} years old next birthday!')
    print(f"We hear you like the color {color.lower()}! {color.lower()} is a string with color")

name = input('Enter your name: ')
age = int(input('Enter your age: '))
color = input('Enter your favorite color:')
greeting(name, age, color)

#Name notation

def greeting(name, age=28, color="red"):
 #Greets user with “name” from “input box” and “age”, if unavailable, default age is used   
   
   print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
   print(f"We hear you like the color {color.lower()}!")

greeting(age=27, name="brian",color="Blue")

#Profile(yob=1995,weight=83.5,height=192,eye_color="blue")


#Return statement
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return f"{amount}, {tax}, {total_amount}" #Return string
    #return [amount, tax, total_amount] #Return a list
    #return {amount, tax, total_amount} #Return a set

    
price = value_added_tax(100)    
print(price, type(price))


# 🪐 Mars Mission Planner — Challenge Steps
#
# 1. Write a function to calculate how long it takes
#    to reach Mars at a given speed.
#    - Mars' average distance is 225,000,000 km.
#    - Use the formula: time = distance ÷ speed
#    - Round the result to the nearest hour.
#
# 2. Write another function to figure out the total fuel cost
#    for a mission.
#    - Formula: total cost = distance × fuel usage × price per liter
#
# 3. Test your functions with the provided mission data:
#    - Pathfinder: 40,000 km/h
#    - Perseverance: 75,000 km/h
#    - Starship: 120,000 km/h
#    - Each mission travels 225 million km,
#      burns 0.3 liters/km, and fuel costs $1.80/L.
#
# 4. For each mission, print a report showing:
#    - Mission name
#    - Travel time (hours)
#    - Total fuel cost

# Mission data
mission_1_speed = 40000  # Pathfinder
mission_2_speed = 75000  # Perseverance
mission_3_speed = 120000 # Starship

mars_distance = 225000000  # in kilometers 
fuel_rate = 0.3              # liters per kilometer
fuel_price = 1.8             # dollars per liter

Pathfinder_travel_time = mars_distance/mission_1_speed
Perseverance_travel_time = mars_distance/mission_2_speed
Starship_travel_time = mars_distance/mission_3_speed

fuel_used = mars_distance * 0.3
fuel_cost = fuel_used * 1.8

print("===== Mars Mission Planner =====\n")
print(f"Mission Name: Pathfinder")
print(f"Mission travel time: {round(Pathfinder_travel_time,1)} hours")
print(f"Mission total fuel cost: {fuel_cost} dolars")
print("")
print(f"Mission Name: Perseverance")
print(f"Mission travel time: {round(Perseverance_travel_time,1)} hours")
print(f"Mission total fuel cost: {fuel_cost} dolars")
print("")
print(f"Mission Name: Starship")
print(f"Mission travel time: {round(Starship_travel_time,1)} hours")
print(f"Mission total fuel cost: {fuel_cost} dolars")
print("")

