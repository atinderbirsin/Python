tup = (1,5,6, 'Harry', True, 34, 35, 235, 2, 543, 435, 45334) # Can contain different types of data, cannot be modified, ordered, indexed, allows duplicates

tup1 = (1)

print(tup)

print(type(tup))

print(tup1)

print(type(tup1))

tup2 = (1,)

print(tup2)

print(type(tup2))

print(tup[0], tup[1], tup[2])

print(tup[-1], tup[-2], tup[-3], tup[-4], tup[-5]) # negative indexing

print(tup[1:4]) # slicing

if "Harry" in tup:
    print('Yes')
else:    
    print('No')

tup3 = (i for i in range(10)) # not a tuple, this is a generator expression

print(tup3) # this will give a generator object

tup[0] = 5 # this will give an error as tuples are immutable

print(tup[15]) # this will give an error as there is no index 15 in the tuple