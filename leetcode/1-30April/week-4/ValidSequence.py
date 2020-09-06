# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, root, arr, idx):
        if idx == len(arr)-1:
            #if leaf return true
            if root.left == None and root.right == None:
                return True
            return False

        result = False
        if root.left != None and root.left.val == arr[idx+1]:
            result |= self.traverse(root.left, arr, idx+1)
        if root.right != None and root.right.val == arr[idx+1]:
            result |= self.traverse(root.right, arr, idx+1)
        return result

    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if len(arr) == 0 or root.val != arr[0]:
            return False
        return self.traverse(root, arr, 0)

test = Solution()
tree = TreeNode(0, TreeNode(1))
print(test.isValidSequence(tree, [0, 1]))
