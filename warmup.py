def myAvg(a, b, c):
    total = 0       # holds the summation
    numbers = 0     # counts the numbers in our range
    for i in range(a, b+1, c):
        total += i
        numbers += 1
    average = total / numbers
    return average

answer = myAvg(1, 10, 1)
print(answer)
assert answer == 5.5, f"expected 5.5, received {answer}"

##user_a = int(input("start: "))
##user_b = int(input("end: "))
##user_c = int(input("step: "))
##answer = myAvg(user_a, user_b, user_c)
##print(answer)
