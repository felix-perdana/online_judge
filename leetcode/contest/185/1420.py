import functools

mod = 1000000007

@functools.lru_cache(maxsize=51*101*51)
def numArrays(n, m, k, lastIndex, maxNum):
    if n == lastIndex:
        if k == 0:
            return 1
        else:
            return 0
    sum = 0
    for i in range(1, maxNum):
        if i > m and k > 0:
            sum += numArrays(n+1, i, k-1, lastIndex, maxNum)
            sum %= mod
        elif i <= m:
            sum += numArrays(n+1, m, k, lastIndex, maxNum)
            sum %= mod
    return sum

def initMemo(n, m, k):
    global memo
    memo = {}

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        initMemo(n, m, k)
        return numArrays(0, 0, k, n, m+1)

test = Solution()
print(test.numOfArrays(2, 3, 1)) #6
print(test.numOfArrays(2, 2, 1)) #3
print(test.numOfArrays(5, 2, 3)) #0
print(test.numOfArrays(9, 1, 1)) #1
print(test.numOfArrays(37, 17, 7)) #418930126
