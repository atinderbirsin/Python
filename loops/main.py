name = input("Enter your name: \n")

for character in name:
    print(character)
    if(character.lower() == 'a'):
        print('This is a vowel')


colors = ['Red', 'Green', 'Blue', 'Yellow']

for color in colors:
    print(color)
    for character in color:
        print(character)

for k in range(1, 2001, 3): # 1 is included but 2001 is not included, and the step is 3
    print(k)

i = 0

while (i < 10):
    print(i + 1)
    i = i + 1

print('\nDone with loops!')

i = 0

while (i < 28):
    i = int(input("Enter a number: \n"))

print('Done with loop', i)