marks = [3,4,5, 'Hary', True, 34, 35, 235, 2, 543, 435, 45334] # Can contain different types of data, can be modified, ordered, indexed, allows duplicates

print(marks)

print(type(marks))

print(marks[0], marks[1], marks[2])

print(marks[-1], marks[-2], marks[-3], marks[-4], marks[-5]) # negative indexing

print(marks[1:4]) # slicing

if "Hary" in marks:
    print('Yes')
else:
    print('No')

if 'arry' in "harry":
    print('Yes')
else:
    print('No')

print(marks[:])

print(marks[1: -1]) # this will become marks[1: 11]

print(marks[1:len(marks)-1]) # this is same as above

print(marks[1:11:2]) # this will give elements from index 1 to 10 with a step of 2

# list comprehension

lst = [i for i in range(10)]

print(lst)

lst1 = [i*i for i in range(10) if i % 2 == 0]

print(lst1)

print(marks[6]) # this will give an error as there is no index 6 in the list
