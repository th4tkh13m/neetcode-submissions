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

        def get_depth(node):
            if not node:
                return 0, True
            
            left_depth, left_balance = get_depth(node.left)
            right_depth, right_balance = get_depth(node.right)

            is_balance = abs(left_depth - right_depth) <= 1 and left_balance and right_balance
            return max(left_depth, right_depth) + 1, is_balance


        _, is_balance = get_depth(root)
        return is_balance