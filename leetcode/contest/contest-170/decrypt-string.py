class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []

        i = 0
        while i < len(s):
            print(i)
            if i+2 < len(s) and s[i+2] == '#':
                x = chr(int(s[i:i+2]) + ord('a') - 1)
                ans.append(x)
                i += 3
            else:
                x = chr(int(s[i]) + ord('a') - 1)
                ans.append(x)
                i += 1

        return "".join(ans)

test = Solution()
print(test.freqAlphabets("10#11#12"))
