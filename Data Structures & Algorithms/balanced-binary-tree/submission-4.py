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
        
        def checkBalanceAndGetDepth(root):
            if not root:
                return True, 0
            
            left_balance, left_depth = checkBalanceAndGetDepth(root.left)
            right_balance, right_depth = checkBalanceAndGetDepth(root.right)

            if not left_balance or not right_balance:
                return False, 0
            
            return -1 <= (left_depth - right_depth) <= 1, 1 + max(left_depth, right_depth)
        return checkBalanceAndGetDepth(root)[0]
