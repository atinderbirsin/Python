age = int(input("Enter your age: \n"))

match(age):
    case age if age < 18:
        print('You cannot drive')
    case age if age > 18 and age < 60:
        print('You can drive')
    case age if age >= 60:
        print('You can drive but be careful')
    case _:
        print('Invalid age')