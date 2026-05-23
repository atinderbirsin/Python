name = '! atinder !!!!!!!! atinder !!!!!!!' # strings are immutable, we cannot change the value of a string
nameOnly = 'atinder'

print(len(name))

print(name.upper()) # to convert all characters to uppercase

print(name.lower()) # to convert all characters to lowercase

print(name.rstrip('!')) # to remove all trailing characters from the right side of the string, in this case we are removing all '!' from the right side of the string

print(name.replace('atinder', 'john')) # to replace all occurrences of a substring with another substring 

print(name.split(' '))

print(nameOnly.capitalize()) # to convert the first character of the string to uppercase and the rest of the characters to lowercase

print(name.count('atinder')) # to count the number of occurrences of a substring in the string

print(name.endswith('!!')) # to check if the string ends with a specific substring, in this case we are checking if the string ends with '!!'


str1 = 'Wecome to the console!!!'

print(str1.endswith('to', 4, 9)) # to check if the substring 'to' is present in the string from index 4 to index 9, in this case it is present at index 7 and index 8 

str3 = '   Hello, World!   32789832'

print('alnum',str3. isalnum()) # to check if all characters in the string are alphanumeric (letters and numbers) and there is at least one character, in this case it returns False because there are spaces and special characters in the string

str4 = 'HelloWorld'

print('isalpha', str4.isalpha()) # to check if all characters in the string are alphabetic (letters) and there is at least one character, in this case it returns True because all characters in the string are letters

str5 = '1234567890'

print('isPrintable', str5.isprintable()) # to check if all characters in the string are printable and there is at least one character, in this case it returns True because all characters in the string are printable

str5 = '1234567890\n'

print('isPrintable', str5.isprintable()) # to check if all characters in the string are printable and there is at least one character, in this case it returns False because there is a newline character in the string which is not printable 

str6 = ' Hello, World!   32789832';

print('isSpace', str6.isspace()) # to check if all characters in the string are whitespace characters and there is at least one character, in this case it returns False because there are non-whitespace characters in the string

str7 = '   '

print('isSpace', str7.isspace()) # to check if all characters in the string are whitespace characters and there is at least one character, in this case it returns True because all characters in the string are whitespace characters

str2 = 'He"s name is Dan. He is a honest man'

str8 = 'World Health Organisation'

print('isTitle', str8.istitle()) # to check if the string is in title case, which means that the first character of each word is uppercase and the rest of the characters are lowercase, in this case it returns True because all words in the string are in title case

str9 = 'Python is initerpreted language'

print('startsWith', str9.startswith('Python')) # to check if the string starts with a specific substring, in this case we are checking if the string starts with 'Python'

str10 = 'Python is a programming language'

print('swapCase', str10.swapcase()) # to convert all uppercase characters to lowercase and all lowercase characters to uppercase

str11 = '   Hello, World!   32789832'

print('titleCase ', str11.title()) # to convert the first character of each word to uppercase and the rest of the characters to lowercase

print(str2.find('is')) # to find the first occurance of the specified sub string

print(str2.find('ishh')) # returns -1 if the specificed sub string doesn't exist

print(str2.index('is')) # it also returns the index os specified substring

print(str2.index('isHH')) # if specified string doesn't exist it gives an exception

