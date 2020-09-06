class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        length = [0]
        farthest = {}
        farthest[0] = 0
        tracker = 0

        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                tracker -= 1
            else:
                tracker += 1
            length.append(tracker)
            farthest[tracker] = i+1

        longestSubstring = 0
        for i in range(len(length)):
            num = length[i]
            longestSubstring = max(farthest[num] - i, longestSubstring)

        return longestSubstring
