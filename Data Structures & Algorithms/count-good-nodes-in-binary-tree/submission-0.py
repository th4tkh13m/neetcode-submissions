# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return 0
        
        def scanGoodNodes(root, node, max_val):
            if not node:
                return None
            if node.val >= max_val:
                self.res += 1
                max_val = node.val
            scanGoodNodes(root, node.left, max_val)
            scanGoodNodes(root, node.right, max_val)
        
        scanGoodNodes(root, root, root.val)
        return self.res
