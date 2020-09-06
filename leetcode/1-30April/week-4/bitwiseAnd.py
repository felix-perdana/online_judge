def convertToBinary(n):
    s = ""
    while n > 0:
        s += str(n%2)
        n //= 2
    return s[::-1]

def convertToNumber(r):
    res = 0
    mul = 1
    for i in reversed(r):
        res += mul * int(i)
        mul *= 2
    return res

class Solution:
    def rangeBitwiseAnd2(self, m: int, n: int) -> int:
        s1 = convertToBinary(m)
        s2 = convertToBinary(n)

        if len(s1) != len(s2):
            return 0

        result = ""
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                result += s1[i]
            else:
                for j in range(i, len(s1)): #pad until finish
                    result += '0'
                break

        return convertToNumber(result)

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        pos = 0
        print("-----------")
        while n > m:
            print(n, m)
            n, m, pos = n >> 1, m >> 1, pos + 1
        print(n, m)
        return m << pos

test = Solution()
print(test.rangeBitwiseAnd(12, 15)) #12
print(test.rangeBitwiseAnd(5, 7)) #4
print(test.rangeBitwiseAnd(0, 1)) #0
print(test.rangeBitwiseAnd(25, 57)) #0
print(test.rangeBitwiseAnd(600000000, 2147483645)) #0
