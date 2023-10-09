max_val = 0
answer = ""
for i in range(5):
    words = input(f"Enter string {i}: ")
    amt = 0

    for j in words:
        amt += 1

    if max_val < amt:
        answer = words
        max_val = amt

print(f"The longest string is {answer} and has {max_val} characters")
