# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.res = True


        def getDepth(root):
            if not root:
                return 0
            left_depth = getDepth(root.left)
            right_depth = getDepth(root.right)
            
            self.res = (abs(left_depth - right_depth) < 2) and self.res
            
            return 1 + max(left_depth, right_depth)
        
        
        if not self.res:
            return False
        getDepth(root)
        return self.res
        

        