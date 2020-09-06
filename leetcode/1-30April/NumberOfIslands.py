from typing import List

def isValid(nr, nc, r, c, visit):
    if nr < 0 or nr >= r:
        return False
    if nc < 0 or nc >= c:
        return False
    if visit[nr][nc]:
        return False

    return True

class Solution:
    dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = []
        for r in grid:
            visitRow = []
            for c in r:
                visitRow.append(False)
            visit.append(visitRow)

        island = 0
        q = []
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if not visit[r][c] and grid[r][c] == '1':
                    island += 1
                    #do bfs
                    visit[r][c] = True
                    q.append((r,c))
                    while q:
                        c_r, c_c = q.pop()
                        #go to all dir
                        for d in self.dir:
                            n_r = c_r + d[0]
                            n_c = c_c + d[1]
                            if isValid(n_r, n_c, len(grid), len(grid[r]), visit) and grid[n_r][n_c] == '1':
                                visit[n_r][n_c] = True
                                q.append((n_r, n_c))

        return island


test = Solution()
print(test.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
[
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]
