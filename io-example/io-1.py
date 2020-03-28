from sys import stdin

for line in stdin:
    if line == '': # If empty string is read then stop the loop
        break
    a, b, c = map(str, line.split())
    b = int(b)
    c = int(c)

    if a == "+":
        print(b+c)
    if a == "-":
        print(b-c)
    if a == "*":
        print(b*c)
    if a == "/":
        print(b//c)
    if a == "%":
        print(b%c)
