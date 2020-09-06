class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left = 0
        right = 0
        for sh in shift:
            if sh[0] == 0:
                left += sh[1]
            else:
                right += sh[1]

        dir = left - right
        dir %= len(s)

        first = 0
        if dir < 0: #dir negative means go to the right: move pointer to the right by len - abs(dir)
            first = len(s) + dir
        else: #dir positive means go to the left: move pointer to the right by dir
            first = dir

        newString = s + s

        last = first+len(s)
        return newString[first:last]
