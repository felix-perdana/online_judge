from typing import List
from collections import defaultdict

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        dict = defaultdict(list)

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                dict[sum].append((i, j))

        #print(dict)

        ans = set()
        for x in dict:
            complement = target - x
            #print(x, complement)
            if complement in dict:
                arr1, arr2 = dict[x], dict[complement]
                for i in range(len(arr1)):
                    for j in range(len(arr2)):
                        elem1, elem2 = arr1[i]
                        elem3, elem4 = arr2[j]

                        if not self.sameElement(elem1, elem2, elem3, elem4):
                            ans.add(tuple(sorted([nums[elem1], nums[elem2], nums[elem3], nums[elem4]])))

        #print(ans)
        return ans

    def sameElement(self, elem1, elem2, elem3, elem4):
        if elem1 == elem2 or elem1 == elem3 or elem1 == elem4:
            return True
        if elem2 == elem3 or elem2 == elem4:
            return True
        if elem3 == elem4:
            return True
        return False

test = Solution()
test.fourSum([1, 0, -1, 0, -2, 2], 0)
test.fourSum([-1,0,1,2,-1,-4], -1)
