"""
given two strings with integers,
create a function that will sum these 2 numbers
without converting them to integer 
"""

def sum(a, b):
    #assumption, is to make the length the same
    if len(a) < len(b):
        a, b = b, a
    #b is always shorter than a
    #pad them with 0
    pad = ""
    for i in range(len(a)-len(b)):
        pad += "0"

    b = pad + b
    print(a, b)

    result = ""
    remainder = 0
    for i in range(len(a)-1, -1, -1):
        x = int(a[i]) + int(b[i]) + remainder
        remainder = 0

        if x > 9:
            remainder = 1
            x -= 10

        result += str(x)
    if remainder == 1:
        result += "1"

    result = result[::-1]
    print(result)



sum(str(3), str(12))
sum(str(9), str(11))
sum(str(1), str(999))
