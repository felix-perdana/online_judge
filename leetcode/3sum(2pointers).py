from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            result=[]
            for i  in range(len(nums)-2):
                if i>0 and nums[i]==nums[i-1]:continue
                if nums[i] > 0 : break
                l,r= i+1, len(nums)-1
                if nums[i] + nums[r] + nums[r-1] < 0 : continue
                while l < r:
                    val= nums[i] + nums[l] + nums[r]
                    if val ==0:
                        result.append([nums[i], nums[l] , nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]: l+=1
                        while l<r and nums[r]==nums[r+1]: r-=1
                    elif val <0:
                        l+=1
                        while l<r and nums[l]==nums[l-1]: l+=1
                    else:
                        r-=1
                        while l<r and nums[r]==nums[r+1]: r-=1
            return(result)
