from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []
        queue.append((sr, sc))

        originalColor = image[sr][sc]
        rowSz = len(image)
        copyImage = image
        visit = {}
        visit[(sr, sc)] = True

        while queue:
            i, j = queue.pop()
            copyImage[i][j] = newColor

            for d in dir:
                nr = i + d[0]
                nc = j + d[1]
                if nr < rowSz and nr >= 0 and nc < len(image[nr]) and nc >= 0: #within range
                    if image[nr][nc] == originalColor and visit.get((nr, nc)) != True:
                        queue.append((nr, nc))
                        visit[(nr, nc)] = True

        return copyImage
