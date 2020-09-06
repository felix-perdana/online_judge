class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s, t = [], []
        for i in S:
            if i == '#':
                if len(s) == 0:
                    continue
                s.pop()
            else:
                s.append(i)

        for i in T:
            if i == '#':
                if len(t) == 0:
                    continue
                t.pop()
            else:
                t.append(i)

        print(s, t)
        return s == t


test = Solution()
print(test.backspaceCompare("aaa", "bbb"))
print(test.backspaceCompare("ab#c", "ad#c"))
print(test.backspaceCompare("ab##", "c#d#"))
print(test.backspaceCompare("a##c", "#a#c"))
print(test.backspaceCompare("a#c", "b"))
