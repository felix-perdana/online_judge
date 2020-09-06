import heapq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        pq = []
        dir = [(1, 0), (0, 1)]
        cr, cc = 0, 0

        rsz = len(grid)
        csz = len(grid[0])

        valGrid = []
        for r in grid:
            rowGrid = []
            for c in r:
                rowGrid.append(None)
            valGrid.append(rowGrid)

        heapq.heappush(pq, (grid[0][0], 0, 0))

        while pq:
            val, r, c = heapq.heappop(pq)
            if valGrid[r][c] == None or val < valGrid[r][c]:
                valGrid[r][c] = val
            else:
                #has been visited
                continue

            if r == rsz - 1 and c == csz - 1:
                #has reached the endstate
                return val

            for d in dir:
                nr = r + d[0]
                nc = c + d[1]
                #if valid move
                if nr < rsz and nc < csz:
                    nval = val + grid[nr][nc]
                    if valGrid[nr][nc] == None or nval < valGrid[nr][nc]:
                        #do something
                        heapq.heappush(pq, (nval, nr, nc))
