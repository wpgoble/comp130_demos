def foo(x):
    """assume x needs to be non-negative"""
    assert type(x) == int or type(x) == float, "We need a number"
    assert x >= 0
        
    return x + 5
##
##
##print(foo("a"))
##assert foo(3) == 8, "Should return 8"

##value = input("Give me a number: ")
##try:
##    value = float(value)
##    value = foo(value)
##    print(value)
##except AssertionError:
##    print("Assertion Error")
##except ValueError:
##    print("We need a number")

my_music = {"80sRock":"Queen", "ClassicRock":["Rush"]}
my_music["alt"] = "Mount Joy"
my_music["ClassicRock"].append("Aerosmith")
my_music["country"] = ["Garth Brooks"]


def create_diction(my_list):
    results = {}
    for student in my_list:
        major = student[0:2]
        name = student[2:]
        if major not in results:
            results[major] = [name]
        else:
            results[major].append(name)
    return results
