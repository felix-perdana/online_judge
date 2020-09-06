t = int(input())

def solve(matrix, n):
    trace, row, column = 0, 0, 0

    for i in range(n):
        trace += matrix[i][i]

        num = {}
        isDuplicate = False
        for j in range(n):
            if num.get(matrix[i][j]):
                isDuplicate = True
            num[matrix[i][j]] = True
        if isDuplicate:
            row += 1

        num = {}
        isDuplicate = False
        for j in range(n):
            currNum = matrix[j][i]
            if num.get(currNum):
                isDuplicate = True
            num[currNum] = True
        if isDuplicate:
            column += 1

    return trace, row, column

for _ in range(1, t+1):
    n = int(input())
    matrix = []

    for i in range(n):
        matrix.append([int(s) for s in input().split(" ")])

    result = solve(matrix, n)
    print("Case #{}: {} {} {}".format(_, result[0], result[1], result[2]))
