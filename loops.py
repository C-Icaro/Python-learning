print("1.*Loops are great*")
print("2.**Loops are great**")
print("3.***Loops are great***")
print("4.****Loops are great****")
print("5.*****Loops are great*****")

i=0
while i < 5:
    i+=1
    print(f"{i}."+ "*"*i + "Loops are awesome" + "*"*i)
    
# Three Loop Questions:
#1. What do I want to repeat?
#  -> message
#2. What do I want to change each time?
#  -> stars
#3. How long should we repeat?
#  -> 5 times


#Exercise:
# ☕ Coffee Order Queue Challenge
# 1. Set up two variables: one for total price, one for drink count
# 2. Start a while True loop
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total price

total_price = 0
drink_count = 0

while True:
    order = input("What is your order? (Done for exit)")
    if order == "latte":
        total_price = total_price + 3.5
        drink_count += 1
        input(f"Your bill is actually: ${total_price}")
    elif order == "americano":
        total_price = total_price + 3.00
        drink_count += 1
        input(f"Your bill is actually: ${total_price}")
    elif order == "espresso":
        total_price = total_price + 2.50
        drink_count += 1
        input(f"Your bill is actually: ${total_price}")
    elif order == "done":
        break
    else:
        input("Put a real order.")
        
print("--Total bill--")
print("Your drink count was: $" + str(drink_count))
print("Your total price was: $" + str(total_price))



#Breack and continue:
friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    if friend == 'Eric':
        print('Found ' + friend + '!')
        continue
        #break
    print(friend)

print("For Loop done!")


#Nesting (loop inside loop):
friends = ['John','Terry','Eric']
for friend in friends:
    for number in [1,2,3]:
        print(friend, number)

print("For Loop done!")

#For loop exercise:
names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

names.extend(names1)
for i in [1, 2]:
    names.append(input("Add extra friend " + str(i)))
for friends in names:
    print(friends.lower().title(), "you are invited for the party.")


