# code snippet for reversing the word "function"
word = "function"
result = ""
for i in range(len(word) - 1, -1, -1):
    result += word[i]
print(word, result)
# encapsulate it to be a function
def reverse_func():
    word = "function"
    result = ""
    for i in range(len(word) - 1, -1, -1):
        result += word[i]
    print(word, result)    
# generalized version
def reverse_func(word):
    result = ""
    for i in range(len(word) - 1, -1, -1):
        result += word[i]
    print(word, result)    

# Problem 2
def count_letter(word, target):
    word = word.lower()
    target = target.lower()
    count = 0
    for letter in word:
        if letter == target:
            count += 1
    return count

# Map Pattern
def map_example(my_list):
    result = []
    for number in my_list:
        result.append(number ** 2)
    return result

# Reduce
def count_odds(my_list):
    count = 0
    for element in my_list:
        if element % 2 != 0:
            count += 1
    return count

# Filter
def remove_odd(my_list):
    result = []
    for element in my_list:
        if element % 2 == 0:
            result.append(element)
    return result

# Recursion
def count_down(n):
    if n == -1:
        print("Blast off!")
    else:
        print(f"{n}...")
        count_down(n - 1)

x = 3
count_down(x)










