# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insert(self, num, bst):
        if bst == None:
            return TreeNode(num)
        if num < bst.val:
            #go to left
            bst.left = self.insert(num, bst.left)
        elif num > bst.val:
            #go to right
            bst.right = self.insert(num, bst.right)
        return bst

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        bst = None
        for p in preorder:
            bst = self.insert(p, bst)

        return bst

test = Solution()
print(test.bstFromPreorder([8,5,1,7,10,12]))
