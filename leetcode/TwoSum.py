from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i, elem in enumerate(nums):
            complement = target - elem
            if complement in dict:
                return [dict[complement], i]
            dict[elem] = i
        return None
