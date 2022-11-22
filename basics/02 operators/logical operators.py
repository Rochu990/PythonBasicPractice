
print(True and True)
print(True and False)
print(False and False)

print(10 >= 5 and 3 < 9)
print(12 < 20 and 5 > 10)
print(3 == 5 and 6 < 1)

taskCompleted = True
linesOfCodeWritten = 100

if taskCompleted == True and linesOfCodeWritten >=50:
    print("Go home")

hourOfDay = 15
if taskCompleted == True and linesOfCodeWritten >= 60 and hourOfDay >= 15:
    print("Again go home now!")

print(True or True)
print(True or False)
print(False or False)

print(10 >= 10 or 5 > 3)
print(5 <= 7 or 5 == 3)
print(2 != 2 or 5 == 5)
print(1 == 3 or 4 > 10)


if 10 > 5 or "Ania" != "Ola":
    print("true or true")

if 3 == 5 or "Ania" == "Ola":
    print("false or false")

print(not True)
print(not False)

print(not(3 == 3))
print(not(5 > 10))
print(not(10 >= 6 and "Ola" != "Ania"))

taskCompleted = False

if taskCompleted == True:
    print("Go Home")

if not taskCompleted:
    print("Stay a bit longer and finish the job")