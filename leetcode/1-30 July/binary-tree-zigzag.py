from typing import List
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        d = deque([(root, 0)])
        m = defaultdict(list)

        while len(d) > 0:
            item = d.popleft()
            curr, level = item[0], item[1]
            m[level].append(curr.val)
            if curr.left != None:  d.append((curr.left, level+1))
            if curr.right != None:  d.append((curr.right, level+1))

        ans = []
        for i in range(len(m)):
            if i%2 == 1:
                ans.append(m[i][::-1])
            else:
                ans.append(m[i])

        return ans
