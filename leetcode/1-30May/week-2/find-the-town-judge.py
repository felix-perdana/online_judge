#there must be a person trusted by everybody except himself
#there's only exactly one person
#he must not trust anyone

from collections import defaultdict
from typing import List

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1

        trusted = defaultdict(set)
        for t in trust:
            trusted[t[1]].add(t[0])

        idx = -1
        for t in trusted:
            numPeople = len(trusted[t])
            if numPeople == N-1:
                if idx != -1:
                    return -1
                idx = t

        for t in trust:
            if t[0] == idx:
                return -1

        return idx
