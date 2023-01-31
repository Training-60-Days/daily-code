# 222-Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        leftDepth = 0; rightDepth = 0
        left = root.left; right = root.right

        while left:
            left = left.left
            leftDepth += 1
        while right:
            right = right.right
            rightDepth += 1


        if leftDepth == rightDepth:
            return pow(2,leftDepth + 1) - 1

        leftCount = self.countNodes(root.left)
        rightCount = self.countNodes(root.right)
        result = leftCount + rightCount + 1

        return result 

#  Time complexity: worst case - O(N), N is numbers of nodes in tree, if tree
# is not a complete tree
#  Space complexity: O(n):  O(h), but worst case is tree is skewed,
#  and each node has one child, so O(n)