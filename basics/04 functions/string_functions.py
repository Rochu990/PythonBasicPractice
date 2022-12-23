
print("Hello " + "World!")
print("hello" * 3)

string = "Hello World!"
print(string[0])
print(string[0:5])

print("Hello" in string)
print("Hello" not in string)

multiline = """line 1
line 2
line 3
"""
print(multiline)

print("ala".capitalize())
print("Ola ma kota, Ola ma psa".count("Ola"))
print("Hello".center(20, "-"))
print(string.startswith("Hello"))
print(string.endswith("World!"))
print(string.find("World!"))
print(string.find("Ola"))
print(("Ola ma kota, Ola ma psa".rfind("Ola")))

print("123456789.2342".isalnum())
print("123456789".isalnum())
print("123456789 k".isalnum())
print("kot".isalnum())
print(" kot".isalnum())
print(" kot2".isalnum())

print("test".islower())
print("test".isupper())
print("Test".isupper())
print("TEST".isupper())
print("test".isspace())
print(" ".isspace())
print(" \n".isspace())

print("-|".join(["Ala", "Ola", "Adam"]))

print("Hello World".lower())
print("Hello World".upper())
print("Hello World".swapcase())

print(" \n \t   Hello World \n\t")
print(" \n \t   Hello World \n\t".lstrip())
print(" \n \t   Hello World \n\t".rstrip())
print(" \n \t   Hello World \n\t".strip())

print("Ola ma psa, Ola ma kota".replace("Ola", "Kasia"))

print("My name is {myName}, I'm from {country}".format(myName = "Przemek", country = "Poland"))
print("My name is {0}, I'm from {1}".format("Przemek", "Poland"))
print("My name is {}, I'm from {}".format("Przemek", "Poland"))