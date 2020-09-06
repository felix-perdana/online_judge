from typing import List

print(-13//10)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        validDict = {}
        mark = "1"
        for i in range(r):
            c = len(board[i])
            for j in range(c):
                if board[i][j] == 'O':
                    #bfs
                    q = [(i, j)]
                    isValid = True
                    while len(q):
                        a, b = q.pop()
                        #if a, b is on the border
                        if a == 0 or a == r-1 or b == 0 or b == c-1:
                            isValid = False
                        board[a][b] = mark
                        for k in dir:
                            nr, nc = a + k[0], b + k[1]
                            if nr >= r or nc >= c or nr < 0 or nc < 0 or board[nr][nc] != 'O':
                                continue
                            q.append((nr, nc))

                    if isValid:
                        validDict[mark] = True
                    mark = str(int(mark)+1)

        for i in range(r):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    continue
                if validDict.get(board[i][j]) != None:
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'
