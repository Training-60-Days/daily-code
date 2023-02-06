# 257-Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def dfs(node, sub):
            sub.append(node.val)
            if node.left is None and node.right is None:
                string = '->'.join(map(str, sub))

                res.append(string)
                sub = []
                return
            
            if node.left:
                dfs(node.left, sub)
                sub.pop()
            if node.right:
                dfs(node.right, sub)
                sub.pop()
            
        dfs(root, [])
        return res

#  Time complexity: worst case - O(N), N is numbers of nodes in tree, if tree
# is not a balanced tree
#  Space complexity: O(n):  O(h), but worst case is tree is skewed,
#  and each node has one child, so O(n)
        