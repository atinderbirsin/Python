age = int(input("Enter your age: \n"))

# Conditional Operators

# <, > , <=, >=, ==, !=

print(age>18)
print(age<18)
print(age>=18)
print(age<=18)
print(age==18)
print(age!=18)

print("Your age is", age)

if(age >= 18):
    print('You can drive')
elif(age >= 16):
    print('You can learn to drive')
else:
    print('You cannot drive') 

num = int(input("Enter a number: \n"))

if(num < 0):
    print("Negative is number")
elif (num == 0):
    print("Number is zero")
elif(num == 999):
    print("Number is special")
elif(num > 0):
    print("Positive is number")

print('I am happy now!')

num1 = int(input("Enter first number: \n"))

if(num1 < 0):
    print('Number is less than zero')
elif(num1 > 0):
    if(num1 < 10):
        print('Number is between 1 and 10')
    elif(num1 > 10 and num1 < 20):
        print('Number is between 11 and 20')
    else:
        print('Number is greater than 20')
else:    
    print('Number is zero')


from datetime import datetime

now = datetime.now()
formatted_time = int(now.strftime('%H'))

if(formatted_time < 12):
    print('Good Morning!')
elif(formatted_time >= 12 and formatted_time < 17):
    print('Good Afternoon!')
elif(formatted_time >= 17 and formatted_time < 21):
    print('Good Evening!')
else:    print('Good Night!')