from typing import List

class Solution:
    def binSearch(self, le, ri, nums, target):
        l, r = le, ri
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m-1
            else:
                l = m+1

        return -1
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        #find the pivot
        l, r = 0, len(nums)-1
        leftNum = nums[0]
        tempPivot = 0
        while l <= r:
            m = (l+r)//2
            if nums[m] < leftNum:
                tempPivot = m
                #try go to the left
                r = m-1
            else: #pivot on the right
                l = m+1

        pivot = tempPivot

        res = max(self.binSearch(0, pivot-1, nums, target), self.binSearch(pivot, len(nums)-1, nums, target))
        return res

test = Solution()
print(test.search([4,5,6,7,0,1,2], 0))
print(test.search([4,5,6,7,0,1,2], 2))
print(test.search([4,5,6,7,0,1,2], 5))
print(test.search([4,5,6,7,0,1,2], 3))
print(test.search([4,5,6,7,0,1,2], 4))
print(test.search([4], 5))
