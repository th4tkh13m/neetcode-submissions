# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_diameter = 0

        def get_depth(node):
            if not node:
                return 0
            
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)

            diameter = left_depth + right_depth

            nonlocal max_diameter
            max_diameter = max(max_diameter, diameter)

            return 1 + max(left_depth, right_depth)

        get_depth(root)
        return max_diameter
