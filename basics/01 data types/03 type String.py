str = "Hello World!"
print(str);
print(len(str))
print(type(str))

print(str[len(str)-1])

print(str[0:5]) #Hello

print(str * 4)

str2 = str + " Adam"
print(str2)

print(str2[6:]) #World! Adam

print(str2[::3]) # co trzeci element

multiLine = """"Pierwsza linia
Druga linia
Trzecia linia
"""
print(multiLine)

multiLine2 = "Pierwsza linia\nDruga linia\nTrzecia \t linia \" \\  "
print(multiLine2) 