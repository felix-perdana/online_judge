# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for c in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]
    costs = []
    for i in range(n):
        costs.append(int(input()))

    print(costs)
    ans = 0
    print("Case #{}: {}".format(c, ans))
  # check out .format's specification for more formatting options
