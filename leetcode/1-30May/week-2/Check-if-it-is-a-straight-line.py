from typing import List

class Solution:
    def check(self, c1, c2, c3):
        return (c1[1]-c2[1]) * (c2[0]-c3[0]) == (c2[1]-c3[1]) * (c1[0]-c2[0])

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        c = sorted(coordinates, key=lambda x: x[0])
        return all([ self.check(c[i], c[i+1], c[i+2]) for i in range(len(c)-2)])

test = Solution()
print(test.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(test.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
