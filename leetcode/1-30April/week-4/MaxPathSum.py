# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def setMaxPath(self, root: TreeNode) -> int:
        if root == None:
            return 0

        mid = root.val
        left = self.setMaxPath(root.left)
        right = self.setMaxPath(root.right)

        maxVal = max(mid, left + mid, right + mid, left + right + mid)
        self.maxVal = maxVal if self.maxVal == None else max(maxVal, self.maxVal)

        bigger = max(left, right)
        return max(bigger + root.val, root.val)


    def maxPathSum(self, root: TreeNode) -> int:
        self.maxVal = None
        self.setMaxPath(root)

        return self.maxVal
