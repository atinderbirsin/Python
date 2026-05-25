def factorial (n):
    if(n == 0 or n ==1):
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))


def fibonacci(n):

    if n < 0:
        return "Invalid input"

    a, b = 0, 1

    for _ in range(n):
        temp = a + b
        a = b
        b = temp

    return a

#  f0 = 0
#  f1 = 1
#  f2 = f0 + f1
#  fn = f(n - 1) + f(n - 2)
# 0 1 1 2 3 5 8

# Remember to break the logic so that we can implement it, here we fn = f(n-1) + f(n-2), we basically inverted the logic  instead of subtracting 1 and 2 , we took the initial values we know f0 = 0 & f1 = 1 then looped till the number we need the f(n) & calculated by adding the last two values.
# We stored the first two values that we have and calculated the next two on the basis of that till the n & adding the we got the result 

print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(5))
print(fibonacci(7))