# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        is_valid = True
        def dfs(node) -> [int, int]:
            if not node:
                return None, None
            
            min_left, max_left = dfs(node.left)
            min_right, max_right = dfs(node.right)
            nonlocal is_valid
            if min_right:
                is_valid = is_valid and node.val < min_right
            if max_left:
                is_valid = is_valid and max_left < node.val 
            min_left = min_left if min_left else node.val
            max_right = max_right if max_right else node.val
            return min_left, max_right
        dfs(root)
        return is_valid