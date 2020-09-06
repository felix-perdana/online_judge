# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    diamter = -1
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        this = self.getHeight(root.left) + self.getHeight(root.right)

        return max(this, left, right)

    def getHeight(self, node: TreeNode) -> int:
        if node == None:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        return max(left, right) + 1
