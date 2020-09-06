class Solution:
    def findComplement(self, num: int) -> int:
        bin = format(num, 'b')
        comp = ""
        for b in bin:
            c = '0'
            if b == '0':
                c = '1'
            comp += c

        return int(comp, 2)

test = Solution()
print(test.findComplement(5))
print(test.findComplement(1))
print(test.findComplement(0))
