# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot :
            return False
        # We check whether any sub root is same tree
        def isSameTree(p, q):
            if not p and not q:
                return True
            if (not p and q) or (not q and p):
                return False
            if p.val != q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        search = isSameTree(root, subRoot) 
        return search or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)