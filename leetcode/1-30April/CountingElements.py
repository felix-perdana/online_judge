from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        dict = {}
        for a in arr:
            dict[a] = True

        count = 0
        for a in arr:
            if dict.get(a+1):
                count += 1

        return count

test = Solution()
print(test.countElements([1,2,3]))
