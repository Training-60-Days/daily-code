# 110-Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def checkHeight(node):
            if not node: return 0
            
            LD = checkHeight(node.left)
            if LD == -1: return -1
            RD = checkHeight(node.right)
            if RD == -1: return -1

            if abs(LD - RD) > 1:
                return -1
            else:
                return max(LD, RD) + 1

        return False if checkHeight(root) == -1 else True

#  Time complexity: worst case - O(N), N is numbers of nodes in tree, if tree
# is not a balanced tree
#  Space complexity: O(n):  O(h), but worst case is tree is skewed,
#  and each node has one child, so O(n)