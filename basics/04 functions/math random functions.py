import math
import random

print(type(str(12)))
print(type(str([12, 34, 56])))

number = int("123")
print(type(number))

number += 10
print(number)


floatNum = float("45.67")
print(type(floatNum))
floatNum = floatNum * 2
print(floatNum)

print(abs(9))
print(abs(-8.67))

print(math.ceil(10.123456789))
print(math.ceil(-1.123456789))
print(math.floor(10.123456789))
print(math.floor(-1.123456789))


print(max(1, 45, 63, 745, -1, 8, 100))
print(max([1, 45, 63, 745, -1, 8, 100]))
print(max((1, 45, 63, 745, -1, 8, 100)))
print(min((1, 45, 63, 745, -1, 8, 100)))
print(min([1, 45, 63, 745, -1, 8, 100]))

print(4 ** 3)
print(pow(4, 3))

print(math.sqrt(14233))

print(round(10.1234566789, 3))
print(round(10.1234566789, 2))
print(round(10.1294566789, 2))

print(random.random())
print(random.random() * 100)
print(int(random.random() * 100))

print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random.choice(["raz", "dwa", "trzy", "cztery"]))
print(random. randrange(0, 10 ,2))

list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(list_data)
print(list_data)