from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        p = points
        n = len(points)
        if n < 3:
            return n

        dict = {}
        for p in points:
            t = (p[0], p[1])
            if dict.get(t) == None:
                dict[t] = 0
            dict[t] = dict[t]+1

        maxVal = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                sameLine = 0
                for k in range(j+1, n):
                    x1, y1, x2, y2, x3, y3 = p[i][0], p[i][1], p[j][0], p[j][1], p[k][0], p[k][1]
                    if (y2-y1) == 0 and (x2-x1) == 0:
                        continue
                    if (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1):
                        sameLine += dict[(x3, y3)]
                sameLine += dict[(p[j][0], p[j][1])] + dict[(p[i][0], p[i][1])]
                maxVal = max(maxVal, sameLine)

        return maxVal
