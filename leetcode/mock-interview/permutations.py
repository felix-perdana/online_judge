from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        result = []
        for k,v in enumerate(nums):
            nextPermute = self.permute(nums[0:k] + nums[k+1: len(nums)])
            for n in nextPermute:
                result.append([v]+n)
        return result


test = Solution()
print(test.permute([1, 2, 3, 4]))
