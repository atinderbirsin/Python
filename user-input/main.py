str = input()
print("You entered: ", str)

name = input("Enter your name: ")
print("Your name is", name)

a = input('Enter first number: \n')
b = input('Enter second number: ')
# without typecasting
print("\nThe sum of", a, "and", b, "is", a + b) 

x = input('Enter first number: \n')
y = input('Enter second number: ')
# using typecasting to convert string to integer
print("\nThe sum of", x, "and", y, "is", int(x) + int(y))