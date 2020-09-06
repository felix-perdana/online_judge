from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        arr = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if arr[i][j] == 1 and i > 0 and j > 0:
                    arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1

        total = 0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                val = arr[i][j]
                total += val

        return total

test = Solution()
test.countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])
test.countSquares([
  [1,0,1],
  [1,1,0],
  [1,1,0]
])
