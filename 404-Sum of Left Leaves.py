404-Sum of Left Leaves
https://leetcode.com/problems/sum-of-left-leaves/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        if root.left is None and root.right is None: return 0

        leftSum = self.sumOfLeftLeaves(root.left)

        if root.left and root.left.left is None and root.left.right is None:
            leftSum += root.left.val

        rightSum = self.sumOfLeftLeaves(root.right)
        
        return leftSum + rightSum
#  Time complexity: worst case - O(N), N is numbers of nodes in tree, if tree
# is not a balanced tree
#  Space complexity: O(n):  O(h), but worst case is tree is skewed,
#  and each node has one child, so O(n)