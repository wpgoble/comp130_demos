# Pig latin translator
# Here is a void function
def pig_latin(word):
    first = word[0]

    if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
        print(word + "way")
    else:
        print(word[1:] + first + "ay")    


# Here is a fruitful version
def pig_latin2(word):
    first = word[0]
    output = ''
    if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
        output = word + 'way'
    else:
        output = word[1:] + first + 'ay'
    return output

    
word2 = "input"
word2 = word2.lower()
pig_latin(word2)
