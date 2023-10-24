import random


# Exercise 1.1 -- String repetition
def repeat(word, amt):
    letter = word[random.randint(0, len(word) - 1)]
    return letter * amt


# Exercise 1.2 -- for loop
def repeat2(word, amt):
    assert type(word) == str, "word is not a string"
    assert type(amt) == int, "amt is not an int"
    assert amt > 0, "amt should be a natural numbers"

    letter = word[random.randint(0, len(word) - 1)]
    result = ""
    for _ in range(amt):
        result += letter
    return result


# Exercise 1.3 -- while loop
def repeat3(word, amt):
    i = 0
    letter = word[random.randint(0, len(word) - 1)]
    result = ""
    #while len(result) < amt:
    while i < amt:
        result += letter
        i += 1
    return result


# Exercise 2
def summation():
    user = input("please get a number greater than 1: ")
    total = 0
    while user.isdigit() is True:
        user = int(user)
        number = random.randint(1, user)
        total += number
        user = input("please get a number greater than 1: ")
    return total


word = "Triangle"
print(repeat(word, 3))
print(repeat2(word, 3))
