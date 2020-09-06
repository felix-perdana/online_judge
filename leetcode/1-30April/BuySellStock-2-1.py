from typing import List
from functools import lru_cache

class Solution:
    prices = []
    memo = []
    cnt = 0

    def resetMemo(self):
        self.memo = []
        n = len(self.prices) + 2
        for i in range(n):
            self.memo.append(-1)

    def solve(self, idx):
        if self.memo[idx] != -1:
            return self.memo[idx]
            self.cnt += 1
        n = len(self.prices)
        maxProfit = 0
        for i in range(idx+1, n):
            currProfit = 0
            if self.prices[i] - self.prices[idx] > 0:
                currProfit = self.prices[i] - self.prices[idx] + self.solve(i)

            maxProfit = max(maxProfit, currProfit)

        self.memo[idx] = maxProfit
        return maxProfit

    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.cnt = 0
        self.resetMemo()

        result = self.solve(0)
        return result

test = Solution()
testArr = [n for n in range(500)]
print(test.maxProfit(testArr))
print(test.maxProfit([7,1,5]))
print(test.maxProfit([7,1,5,3,6,4]))
print(test.maxProfit([1,2,3,4,5]))
print(test.maxProfit([7,6,4,3,1]))
