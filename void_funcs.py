##def print_twice(string):
##    x = string * 2
##    print(x)
##    print(x)
##
##
##result = print_twice('Bing')
##print(result)
def sum_square(x):
    answer = 0
    for i in range(1, x+1):
        answer += i
    answer = answer ** 2
##    print(answer)
    return answer

val = input("Please type a number ")
val = int(val)
print_val = sum_square(val)
print(print_val)
print(answer)
