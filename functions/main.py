a = 9
b = 8

gmean1 = (a * b) / (a + b)

print(gmean1)

c = 8 

d = 7

gmean2 = (c * d) / (c + d)

print(gmean2)


def calculateGmean(x,y):
    mean = (x * y) / (x + y)
    print(mean)

calculateGmean(9,8)

def isGreater(x,y):
    if (x > y):
        print('First is greater than second')
    else:
        print('Second is greater than first')

isGreater(9,8)
isGreater(8,9) 

def isLesser(x,y):
    pass # this is a placeholder for the function body, it does nothing

def average(x = 4,y = 6):
    print('Average is', (x+y)/2)

average(9,8) 
average()
average(5)
average(y = 5)

def average2(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print('Average is', sum/len(numbers))

average2(9,8,7,6,5)