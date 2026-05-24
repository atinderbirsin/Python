l = [11,5,1,2,4,6,5]

print(l)

l.append(7) # this will add 7 to the end of the list

print(l)

l.sort() # this will sort the list in ascending order

print(l)

l.reverse() # this will reverse the list

print(l)

print(l.index(5)) # this will give the index of the first occurrence of 5 in the list 

print(l.count(5)) # this will give the count of 5 in the list

m = l; # this will create a reference to the same list, not a copy

n = l.copy() # this will create a copy of the list

# m[0] = 0 # Not good approach it manipulates the original string

n[0] = 0

print(l) # this will show the change made through m, as m and l refer to the same list
print(n) # this will not show the change made through m, as n is a copy of the list
print(m) # this will show the change made through m, as m and l refer to the same list

l.insert(1, 899) # this will insert 899 at index 1

print(l)

k = l + m # this will concatenate the two lists

k2 = l.copy() + m.copy() # this will concatenate the two lists after copying them, so that changes to l and m will not affect k2

l[0] = 0 # this will change the first element of the list to 0

print('k2:',k2)

print('k:',k) # this will show the change made through l, as k is a new list created by concatenating l and m
 
l.extend(n) # this will extend the list by adding elements from the iterable
print(l)