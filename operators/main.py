print(15 + 6) # addition
print(15 - 6) # subtraction
print(15 * 6) # multiplication
print(15 / 6) # division
print(15 % 6) # modulus
print(15 // 6) # floor division
print(5**3) # exponentiation

# Calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Which operation do you want to perform?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Floor Division")
print("7. Exponentiation")

choice = int(input("Enter your choice (1-7): "))

if choice == 1:
    print("Result: ", num1 + num2)
elif choice == 2:
    print("Result: ", num1 - num2)
elif choice == 3:
    print("Result: ", num1 * num2)
elif choice == 4:
    print("Result: ", num1 / num2)
elif choice == 5:
    print("Result: ", num1 % num2)
elif choice == 6:
    print("Result: ", num1 // num2)
elif choice == 7:
    print("Result: ", num1 ** num2)
else:    print("Invalid choice!")