
a = [3,7,42]
b = a
print(a == b)
print(a is b) 
print(id(a), id(b))

a=7
b=3
print('a == b is', a == b)
print('a != b is', a != b)
print('a > b is', a > b)
print('a < b is', a < b)
print('a >= b is', a >= b)
print('a <= b is', a <= b)
print('o in John is ','o' in 'John') #membership
print('o in John is ','o' not in 'John') #non membership
print('John is John ','John' is 'John') #identity
print('John is not John is ','John' is not 'John') # negative identity