101-Symmetric Tree
https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def compare(leftN, rightN):
            if not leftN and not rightN: return True
            if not leftN and rightN: return False
            if leftN and not rightN: return False
            if leftN.val != rightN.val: return False

            outside = compare(leftN.left, rightN.right)
            inside = compare(leftN.right, rightN.left)
            return outside and inside
        return compare(root.left, root.right)
        
#  Time complexity: O(N), N is numbers of nodes in tree
#  Space complexity: O(n):  O(h), but worst case is tree is skewed,
#  and each node has one child, so O(n)