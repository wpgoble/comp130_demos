def palindrome(word):
    assert type(word) == str, f"{word} needs to be a string"
    
    word = word.lower()
    reversed = ""
    for letter in word:
        reversed = letter + reversed
    if reversed == word:
        return "Yes"
    else:
        return "No"

dogTest = palindrome("dog")
assert dogTest == "No", "dog is not a palindrome"
assert palindrome("racecar") == "Yes", "racecar is a palindrome"
print("We have no errors")
