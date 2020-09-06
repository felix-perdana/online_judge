class Solution:
    def isHappy(self, n: int) -> bool:
        x = str(n)
        dict = {}

        while True:
            if dict.get(x) == True:
                break
            dict[x] = True

            sum = 0
            for c in x:
                sum += int(c) ** 2
            if sum == 1:
                return True
            x = str(sum)

        return False

obj = Solution()
for x in range(100):
    print("{}: {}".format(x, obj.isHappy(x)))
