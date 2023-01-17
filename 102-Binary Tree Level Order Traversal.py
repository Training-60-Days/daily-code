102-Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = [root]
        res = []
        
        while q:
            size = len(q)
            res.append([])
            while size:
                node = q.pop(0)
                res[len(res) - 1].append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                size -= 1
            
        return res

#  Time complexity: O(N), N is numbers of nodes in tree
#  Space complexity: O(h):  h is the height of the tree, 
#  but worst case is tree is skewed, and each node has one child, 
#  so O(n), h is n 