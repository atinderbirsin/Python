letter = "Hey my name is {} and I am from {}" # Doesn't work anymore

country = 'India'

name = 'Atinder'

letter.format(name, country)

print(letter)

print(f'Hey my name is {name} and I am from {country}')

print(f'I want to use f-string like as it is: Hey my name is {{name}} and I am from {{country}}')

price = 34.23688

str = f'Price of mango is {price:.2f}'

print(str)

print(f'{2 * 30}')