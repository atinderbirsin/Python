name = input("Enter your name: \n")
length = len(name)
print(name[0:5], length) # inlcuding 0 but not including 5
print(name[:5], length) # inlcuding 0 but not including 5
print(name[0:], length) # including 0 and including all characters after 0
print(name[:], length) # including all characters
print(name[-1: -3]) # invalid len(name) -1 = 6 and len(name) -3 = 4, 6:4
print(name[-3: -1]) # including len(name) -3 = 4 but not including len(name) -1 = 6, 4:6
print(name[-3:]) # including len(name) -3 = 4 and including all characters after len(name) -3 = 4

nam = 'Harry'
print(nam[-4:-2])