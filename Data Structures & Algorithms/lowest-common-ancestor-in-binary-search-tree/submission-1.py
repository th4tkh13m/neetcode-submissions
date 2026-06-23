# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # traverse:
        # root < min(p,q) => move right
        # root > max(p,q) => move left
        # continue until root is in between
        while root.val < min(p.val, q.val) or root.val > max(p.val, q.val):
            if root.val < min(p.val, q.val):
                root = root.right
            else:
                root = root.left
        
        return root