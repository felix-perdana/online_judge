from typing import List
from collections import defaultdict

def getKey(s):
    sortedString = sorted(s)
    print(sortedString)
    print(tuple(sortedString))
    return ''.join(sortedString)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for s in strs:
            #getKey(s)
            dict[tuple(sorted(s))].append(s)

        return dict.values()

test = Solution()
print(test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
