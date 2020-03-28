from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        x = [0]
        for i in range(len(arr)):
            print(arr[i])
            print(x[i])
            x.append(arr[i] ^ x[i])

        ans = []
        for q in queries:
            ans.append(x[q[0]] ^ x[q[1]+1])

        return ans

test = Solution()
print(test.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))
