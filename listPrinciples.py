#List principles:
friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)
friends.sort()#Sort the list, the min first, the max at the end.
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()#Reverse the list
print(friends)
friends.append('TerryG')#Add at the end
print(friends)
friends.insert(1,'TerryG')#Add in a position
print(friends)
friends.extend(cars)#Add cars into friends
print(friends)
friends.remove('Terry')#Removes the guy by the string
print(friends)
friends.pop(2)#Removes the guy by the index
print(friends)

#friends.clear()
#del friends
del friends[2]#Remove by deleting
print(friends)

new_friends = friends.copy()#Copy a list
#new_friends = friends[:]# Also copy a list
#new_friends = list(friends)# Also copy a list

print(friends)
print(new_friends)

#List exercise
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

sales_w2.append(int(input("How much do you earn today?")))

sales = sales_w1 + sales_w2
#sales.extend(sales_w1)
#sales.extend(sales_w2)

print(f"In your best day you earned: US${max(sales)}")
print(f"In your worst day you earned: US${min(sales)}")
print(f"In all days you earned: US${sum(sales)}")



#Split and join

#.split transforms a string in a list. Otherwise .join transforms a list in a string.

msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split())#Split string into a list
print(msg.split(' '))#Split string into a list considering what is in the apostrophes  

print(friends_list)#Print with the bracket
print(str(friends_list))#Also print with the bracket

print('-'.join(friends_list))#Split considering the apostrophes and print.

print(''.join(msg.split()))#Removes all the spaces with split and join
print(msg.replace(" ", ""))#Make the same thing with replace method


#Split and join exercise

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

friends_list.clear()

csv = csv.split(":")
print("In list:", csv)
csv = ",".join(csv)
print("In string:", csv)
csv = csv.split(";")
print("In list:", csv)
csv = ",".join(csv)
print("In string:", csv)
csv = csv.split(",")
print("In list:", csv)

friends_list = csv
print("")
print(f"Your friend are: {', '.join(friends_list)}")


#friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',') #Same thing in one line.

#print('replace', csv.replace(';',',').replace(':',',').split(',')) #Same thing with replace method


#Tuples - faster Lists you can't change
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
print(friends[2:4])
print(friends_tuple[2:4])

#Sets - blazingly fast unordered Lists 
#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()

friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends_set.union(my_friends_set))


#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
#1
print('Eric' and 'John' in friends)

#2
all_friends = ",".join(friends) + ",".join(my_friends) #This way creates a string
print(all_friends, type(all_friends))

print(friends.union(my_friends))#This way maintain the set 
print(friends | my_friends)#Same thing

#3
print(friends.intersection(my_friends))
print(friends & my_friends)

#4
print(friends.difference(my_friends))
print(friends - my_friends)

#5
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)

#6
new_cars = set(cars)
print(new_cars)



# https://www.geeksforgeeks.org/python/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/
