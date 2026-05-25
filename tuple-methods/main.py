countries = ('Spain', 'Italy', 'India', 'England', 'Germany')

temp = list(countries)

temp.append('Russia') # Add Item

temp.pop(3) # Remove Item

temp[2] = 'Finalnd' # Change Item

countries = tuple(temp)

print(countries)

countries1 = ('Pakistan', 'Afghanistan', 'Srilanka', 'Bangladesh')

countries2 = ('Vietnam', 'India', 'China')

southAsia = countries1 + countries2

print(southAsia) 

print(countries.count('Italy'))

print(countries.index('Italy'))

tup = (0, 1, 4, 5, 6, 8, 3, 6 ,4 ,3 ,8 ,9)

print(tup.index(3,4,8))

print(len(tup))

