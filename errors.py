# Syntax Errors
##ten = 6 + 4
##user = input("Please give me a number")
##answer = (1 + 3) / int(user)
##print(float(answer))

# Runtime Errors
##float_num = input("Please give me a floating point number: ")
##int_num = int(float_num)
##print(int_num)
##print("5" * 5)

# Semantic Errors
def tip_calc(bill):
    tip = bill * 0.18
    tip = round(tip, 2)
    print(tip)
    return bill + tip

total = tip_calc(27)
print(total)
