# written by Prof. Goble

def greeting():
    # First we greet the user
    print("Hello! Today we will test if a word is a palindrome.")
    print("A palindrome is a word that is the same forward and backwards")


def pal_test():
    # ask for user input
    word = input("Please provide a word to test: ")

    length = len(word)  # get the length of the user's word
    isPal = True  # Creates flag for later testing
    for i in range(length):
        end = length - (i + 1)
        if word[i] != word[end]:
            isPal = False

    # uses flag to print out if we have a palindrome
    if isPal:
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome!")

def palindrome():
    greeting()  # here we call our greeting function
    pal_test()  # here we call pal_test


palindrome()
