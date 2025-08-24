msg = "lets try to write some code"

print(msg)

print(msg[0].title())#Print first letter

print(msg[-1].title())#Print last letter (second reverse)

print(msg[::-1].title())#Print string in reverse

print(msg.find("try"))#Find position in string

print("try" in msg)#Ask if string is in other

print("try" not in msg)

print(msg.replace("try", "go"))#Replace in string

name=input('What is your name?:')
age=input('What is your age?:')
print(name)

# - Exercise: Create a distance converter converting miles to Km
# - Take two inputs from user: Their first name and the distance in miles
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input("What's your name?: ")
distance = float(input("How many miles do you rode?: "))

distance_km = distance*1.609

print("Congrats ",  name.title(), "!!, You rode ", distance_km, "km.") #Add with coma
print("Best congrats " + name.title() + "!!, You rode " + str(distance_km) + "km.") #Add with plus sign
print(f"Ultra congrats {name.title()}!!, You rode {str(distance_km)}km.") #Add with f sintax





# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

total_race_time = float(input("What's the total race time?"))
pit_stops = float(input("How many pit stops were made?"))
pit_stops_time = float(input("What is the average pit stop duration (in seconds)?"))

total_pit_time= pit_stops*pit_stops_time
percentage_in_pits= total_pit_time/total_race_time*100

print("The total pit stop time was: " + str(total_pit_time) + "seconds")
print("The percentage of race time spent in pits", str(round(percentage_in_pits, 2)) + "%")
if percentage_in_pits > 5:
    print("You need a new pit crew. 🛠️")
else:
    print("You don't need a new pit crew. 🛠️")
