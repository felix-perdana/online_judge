# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for c in range(1, t + 1):
    n = int(input())
    stones = input()

    a, b = 0, 0
    for s in stones:
        if s == 'A':  a += 1
        else:  b += 1

    ans = "Y" if abs(a-b) == 1 else "N"
    print("Case #{}: {}".format(c, ans))
  # check out .format's specification for more formatting options
