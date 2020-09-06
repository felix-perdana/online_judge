from typing import List

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        #run Kadane's algorithm once to find the lowest number
        sum, lowestSum, lowestIndex = 0, 30000*30001, -1
        for i, a in enumerate(A):
            sum = sum+a

            if sum < lowestSum:
                lowestIndex = i
                lowestSum = sum

        #run Kadane's algorithm starting from lowestIndex+1
        arr = A + A
        sum = 0
        maxSum = -30000*30001
        for i in range(lowestIndex+1, lowestIndex+1+len(A)):
            sum = sum + arr[i]
            if arr[i] > sum:
                sum = arr[i]
            maxSum = max(maxSum, sum)


        return maxSum

class Solution2:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        arr = A + A
        finalSum = -30000*30001
        idx = -1
        for i, a in enumerate(A):
            sum = 0
            maxSum = -30000*30001
            for j in range(i, i+len(A)):
                sum = sum + arr[j]
                if arr[j] > sum:
                    sum = arr[j]
                maxSum = max(sum, maxSum)
            if maxSum > finalSum:
                finalSum = maxSum
                idx = i

        return finalSum

print(max(None, 0))
test = Solution()
print(test.maxSubarraySumCircular([1, 2, 3, 4]))
print(test.maxSubarraySumCircular([5, -3, 5]))
print(test.maxSubarraySumCircular([-36,173,-160,207,-151])) #810
