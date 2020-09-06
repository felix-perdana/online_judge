# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for c in range(1, t + 1):
    n = int(input())

    tree = []
    for i in range(n):
        p, h = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        tree.append((p, h))

    tree.sort()
    right = {}
    left = {}
    for i in range(n):
        right[tree[i][0]+tree[i][1]] = tree[i][1]
        left[tree[i][0]-tree[i][1]] = tree[i][1]

    for i in range(n):
        prev = 0 if right.get(tree[i][0]) == None else right[tree[i][0]]
        length = tree[i][1] + prev
        right[tree[i][0]+tree[i][1]] = max(right[tree[i][0]+tree[i][1]], length)

    for i in reversed(range(n)):
        prev = 0 if left.get(tree[i][0]) == None else left[tree[i][0]]
        length = tree[i][1] + prev
        left[tree[i][0]-tree[i][1]] = max(left[tree[i][0]-tree[i][1]], length)

    ans = 0
    for i in left:  ans = max(ans, left[i])
    for i in right:
        ans = max(ans, right[i])
        if left.get(i) != None:
            ans = max(ans, right[i] + left[i])

    print("Case #{}: {}".format(c, ans))
