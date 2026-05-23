# Strings are sequences of characters. They can be defined using single quotes, double quotes, or triple quotes.
name = 'Atinder'

multiple_line_string = '''This is a multiple line string. 
It can span across multiple lines.'''

print('Hello,', name) # Hello, Atinder
print(multiple_line_string)

print(name[0]) # A
print(multiple_line_string[0]) # T

for character in name:
    print(character)