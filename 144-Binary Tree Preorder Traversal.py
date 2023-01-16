144-Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if node is None: return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

#  Time complexity: O(N), N is numbers of nodes in tree
#  Space complexity: O(N), N is numbers of nodes in tree 
# (average case is O(logN), height of tree)
