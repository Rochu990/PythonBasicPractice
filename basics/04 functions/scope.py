number = 12

def test1():
    print(number)

test1()

def test2():
    number = 100
    print(number)
    if 1 == 1:
        print(number)
        if 2 == 2:
            number = 50
            print(number)
    print(number)

test2()

print(number)



def test3():
    global number
    number = 5
    print("test3", number)
    if 1 == 1:
        number = 6
        print("test3", number)

test3()
print("global number after test3()", number)

number = 10

def test4(number):
    print("test4 param: ", number)
    number = 20
    print("test4 after change", number)

test4(33)
print("number after test4() ", number)

print("\nprzerwa\n")

number = 10

def foo():
    print("foo(): ", number)

def bar():
    number = 9
    print("bar() number: ", number)
    foo()

bar()
print("global number after foo() bar() :", number)

print("\nprzerwa\n")

number = 10

def check1():
    number = 12
    print("check1() number: ", number)
    def check2():
        print("chech2(): ", number)
    check2()

check1()
print("global number after check1(): ", number)

print("\nprzerwa\n")

if 1 == 1:
    data = 100

print("data in global scope: ", data)

if 2 == 1:
    next_data = 15

# print("next_data in global scope: ", next_data) #błąd
