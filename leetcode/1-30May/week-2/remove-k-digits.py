class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        removed = [False] * len(num)
        while k:
            prevNum = None
            isRemoved = False
            for i, j in enumerate(num):
                if removed[i]:
                    continue

                if prevNum != None and int(j) < int(num[prevNum]):
                    removed[prevNum] = True
                    k -= 1
                    isRemoved = True
                    break
                prevNum = i
            if not isRemoved:
                break

        for i in reversed(range(len(removed))):
            if k == 0:
                break

            if not removed[i]:
                removed[i] = True
                k -= 1

        res = ""
        for i, j in enumerate(removed):
            if not j:
                res += num[i]

        if len(res) == 0:
            res = "0"
        return str(int(res))


class Solution2:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and len(stack) > 0 and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"



test = Solution()
print(test.removeKdigits("1432219", 3)) #1219
print(test.removeKdigits("10200", 1)) #200
print(test.removeKdigits("10", 2)) #0
print(test.removeKdigits("112", 1)) #11

123456789
