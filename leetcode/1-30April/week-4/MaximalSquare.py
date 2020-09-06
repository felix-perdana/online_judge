from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = 0 if row == 0 else len(matrix[0])

        dp = []
        for i in range(row):
            dp.append([0] * col)

        maxSquare = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    diagonal = 0 if i-1 < 0 or j-1 < 0 else dp[i-1][j-1]
                    prevRow = 0 if i-1 < 0 else dp[i-1][j]
                    prevCol = 0 if j-1 < 0 else dp[i][j-1]
                    dp[i][j] = min(diagonal, prevRow, prevCol) + 1
                    maxSquare = max(maxSquare, dp[i][j])
                else:
                    dp[i][j] = 0

        return maxSquare * maxSquare
