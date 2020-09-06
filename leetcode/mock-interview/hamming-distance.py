class Solution:
    def toBinary(self, x):
        bin = ""
        copy = x
        while copy > 0:
            bin += str(copy % 2)
            copy //= 2
        return bin[::-1]

    def pad(self, x, y):
        diff = abs(len(x)-len(y))
        pad = ""
        for i in range(diff):
            pad += "0"

        if len(x) > len(y):
            y = pad + y
        else:
            x = pad + x
        return x, y

    def hammingDistance(self, x: int, y: int) -> int:
        binX = self.toBinary(x)
        binY = self.toBinary(y)
        binX, binY = self.pad(binX, binY)

        ans = 0
        for k,v in enumerate(binX):
            if binX[k] != binY[k]:
                ans += 1

        return ans

test = Solution()
print(test.hammingDistance(3, 6))
