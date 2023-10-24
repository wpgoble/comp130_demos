import answer as ans

isGuessing = True

while isGuessing:
    name = input("Please guess a name: ")
    if name == ans.child:
        print("Good job")
        isGuessing = False
    else:
        print("Incorrect")
