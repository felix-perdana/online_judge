from typing import List
from functools import lru_cache

class Solution:
    prices = []
    memo = []

    def resetMemo(self):
        sz = len(self.prices)+2
        self.memo = [[] for i in range(sz)]
        for i in range(sz):
            for j in range(sz):
                self.memo[i].append(-1)

    def solve(self, idx, have):
        if self.memo[idx][have] != -1:
            print("masuk")
            return self.memo[idx][have]
        n = len(self.prices)
        if idx == n:
            return 0

        #option 1: sell
        if have == n or (self.prices[idx] - self.prices[have] <= 0):
            sell = 0 #you cannot sell
        else:
            sell = self.solve(idx+1, n) + self.prices[idx] - self.prices[have]

        #option 2: buy
        if have == n:
            buy = self.solve(idx+1, idx)
        else:
            buy = 0 #you cannot buy

        #option 3: skip
        skip = self.solve(idx+1, have)

        self.memo[idx][have] = max(sell, buy, skip)
        return self.memo[idx][have]

    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.resetMemo()
        for i in range(len(prices)-1, 0, -1):
            self.solve(i, len(prices))
        result = self.solve(0, len(prices))
        return result

test = Solution()
testArr = [n for n in range(10, 0, -1)]
print(test.maxProfit(testArr))
#print(test.maxProfit([7,1,5]))
#print(test.maxProfit([7,1,5,3,6,4]))
#print(test.maxProfit([1,2,3,4,5]))
#print(test.maxProfit([7,6,4,3,1]))
