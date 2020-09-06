from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict_p = Counter(p)
        dict_s = Counter(s[:len(p)-1])

        ans = []
        _p, _s = len(p), len(s)

        init = 0
        for i in range(_p-1, _s):
            dict_s += Counter(s[i])
            if len(dict_s - dict_p) == 0:
                ans.append(init)

            dict_s -= Counter(s[init])
            init += 1

        return ans

test = Solution()
print(test.findAnagrams("abab", "ab"))
