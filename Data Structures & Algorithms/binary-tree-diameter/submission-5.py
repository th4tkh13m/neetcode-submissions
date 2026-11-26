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
        def get_diameter(root):
            if not root:
                return 0, 0
            else:
                max_dia_left, max_depth_left = get_diameter(root.left)
                max_dia_right, max_depth_right = get_diameter(root.right)
                depth = 1 + max(max_depth_left, max_depth_right)
                dia = max(max_dia_left, max_dia_right, max_depth_left + max_depth_right)
                return dia, depth
        dia, depth = get_diameter(root)
        return dia
        
        


        