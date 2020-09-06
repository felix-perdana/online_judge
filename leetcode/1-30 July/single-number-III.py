from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        both = 0
        for n in nums:
            both ^= n

        #now both contains the result of the xor of the 2 numbers we are looking for
        firstBitOn = 0
        for i in range(32):
            if (1<<i) & both > 0:
                firstBitOn = 1<<i

        first = 0
        for n in nums:
            if n & firstBitOn > 0:
                first ^= n #remember, duplicate number will always cancel each other

        second = both ^ first
        return [first, second]

test = Solution()
print(test.singleNumber([1,2,1,3,2,5]))
print(test.singleNumber([3, 3, 8, 13, 11, 8]))
