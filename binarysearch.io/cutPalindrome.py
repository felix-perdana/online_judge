import coll
def isPalindrome(a, b):
    c = a + b
    i, j = 0, len(c)-1

    while i <= j:
        if c[i] != c[j]:
            return False
        i += 1
        j -= 1

    return True

class Solution:
    def solve(self, ax, bx):
        # Write your code here
        a = deque
        for i in range(len(a)+1):
            strA = a[0:i]
            strB = b[i:len(b)]
            if isPalindrome(strA, strB):
                return True

        return False

obj = Solution()
print(obj.solve("bzzb", "ivbz"))
