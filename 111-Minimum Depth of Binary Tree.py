111-Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        LH = self.minDepth(root.left)
        RH = self.minDepth(root.right)

        if root.left is None and root.right is not None:
            return 1 + RH
        if root.left is not None and root.right is None:
            return 1 + LH

        return min(LH, RH) + 1

#  Time complexity: O(N), N is numbers of nodes in tree
#  Space complexity: O(n):  O(h), but worst case is tree is skewed,
#  and each node has one child, so O(n)
