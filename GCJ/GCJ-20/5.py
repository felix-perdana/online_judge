matrix = [[] for i in range(51)]

def generateMatrix(idx, n, availNumInRow, usedNumberInCol, res, c):
    if idx == n * n:
        matrix[n].append(res)
        return True

    currRow, currCol = idx//n, idx%n

    arr = []
    if currRow == currCol:
        mustHave = int(c[currCol])
        if mustHave in availNumInRow[currRow] and mustHave not in usedNumberInCol[currCol]:
            arr.append(mustHave)
    else:
        for i in availNumInRow[currRow]:
            if i not in usedNumberInCol[currCol]:
                if int(c[currCol]) != i:
                    arr.append(i)

    for i in arr:
        availNumInRow[currRow].remove(i), usedNumberInCol[currCol].add(i)
        res.append(i)
        hasResult = generateMatrix(idx+1, n, availNumInRow, usedNumberInCol, res[0:], c)
        availNumInRow[currRow].add(i), usedNumberInCol[currCol].remove(i)
        res.pop()
        if hasResult == True:
            return True

t = int(input())

def toString(arr, n):
    for x in range(len(arr)):
        if (x+1)%n == 0:
            print(arr[x])
        else:
            print(arr[x], end = ' ')

allConstraints = [[] for i in range(2500)]

def getConstraints(n, k, s, cnt, target):
    if n == 0:
        if k == 0:
            allConstraints[target].append(s)
        return

    if k <= 0:
        return

    for x in range(1, cnt+1):
        result = s
        if len(s) > 0:
            result += " "
        getConstraints(n-1, k-x, result + str(x), cnt, target)

for _ in range(1, t+1):
    n, k = [int(s) for s in input().split(" ")]
    getConstraints(n, k, "", n, k)
    constraint = []
    for i in allConstraints[k]:
        constraint.append(i.split(" "))

    if not matrix[n]:
        availNumInRow = []
        for i in range(n):
            unique = set()
            for j in range(1, n+1):
                unique.add(j)
            availNumInRow.append(unique)
        usedNumberInCol = [set() for i in range(n)]

        hasFound = False
        for c in constraint:
            hasFound = generateMatrix(0, n, availNumInRow, usedNumberInCol, [], c)
            if hasFound:
                break

    if not hasFound:
        print("Case #{}: {}".format(_, "IMPOSSIBLE"))
    else:
        print("Case #{}: {}".format(_, "POSSIBLE"))
        toString(matrix[n][0], n)
