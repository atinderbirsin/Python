for i in range(12):
    if (i == 10):
        break
    print('5 * ', i + 1, ' = ', 5 * (i + 1))

for i in range(12):
    if (i == 10):
        print('skip the iteration')
        continue 
    print('6 * ', i + 1, ' = ', 6 * (i + 1))

print('loop is over') 

i = 0
while True:
    print(i)
    i = i + 1
    if (i == 10):
        break