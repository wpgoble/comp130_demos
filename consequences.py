foo = int(input("Please provde me a number: "))


def func1():
    global foo
    if foo % 2 == 0:
        foo = 1
        print(f"foo == {foo}")


def func2():
    global foo
    if foo % 2 == 1:
        foo = 7
        print(f"foo == {foo}")


func1()
func2()
