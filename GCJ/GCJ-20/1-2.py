t = int(input())

for _ in range(1, t+1):
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append([int(s) for s in input().split(" ")])

    trace = 0
    badRow, badColumn = 0, 0
    for i in range(n):
        row = set()
        column = set()
        for j in range(n):
            if i == j:
                trace += matrix[i][j]
            row.add(matrix[i][j])
            column.add(matrix[j][i])
        if len(row) != len(matrix[i]):
            badRow += 1
        if len(column) != len(matrix[i]):
            badColumn += 1

    print("Case #{}: {} {} {}".format(_, trace, badRow, badColumn))
