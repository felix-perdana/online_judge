t = int(input())

def solve(act, n):
    result = ""

    C = -1, -1
    J = -1, -1
    for i in range(n):
        isC, isJ = False, False
        start, end = act[i][0], act[i][1]

        if (start < C[0] and end <= C[0]) or (start >= C[1] and end >= C[1]):
            isC = True
        if (start < J[0] and end <= J[0]) or (start >= J[1] and end >= J[1]):
            isJ = True

        if isC:
            result += 'C'
            C = act[i][0], act[i][1]
        elif isJ:
            result += 'J'
            J = act[i][0], act[i][1]
        else:
            result = "IMPOSSIBLE"
            break

    return result

def takeStart(act):
    return act[0]

for _ in range(1, t+1):
    n = int(input())
    activity = []
    for i in range(n):
        inp = input() + " " + str(i)
        activity.append([int(s) for s in inp.split(" ")])

    sortedActivity = sorted(activity, key=takeStart)
    result = solve(sortedActivity, n)

    #do some mapping
    if result != "IMPOSSIBLE":
        map = {}
        for c in range(len(result)):
            key = str(sortedActivity[c][0]) + str(sortedActivity[c][1]) + str(sortedActivity[c][2])
            val = result[c]
            map[key] = val

        result = ""
        for c in range(n):
            key = str(activity[c][0]) + str(activity[c][1]) + str(activity[c][2])
            val = map.get(key)
            result += val

    print("Case #{}: {}".format(_, result))
