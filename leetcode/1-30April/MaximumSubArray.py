class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxSubArray = None
        for x in nums:
            sum += x
            if x > sum:
                sum = x

            if maxSubArray == None:
                maxSubArray = sum
            maxSubArray = sum if sum > maxSubArray else maxSubArray

        return maxSubArray
