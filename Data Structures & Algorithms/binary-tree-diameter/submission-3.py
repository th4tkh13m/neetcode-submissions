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

        def dfs(node, depth):
            if not node:
                return depth
            
            
            # depth += 1
            
            left_depth = dfs(node.left, depth) 
            right_depth = dfs(node.right, depth)
            
            nonlocal max_diameter
            diameter = left_depth + right_depth
            max_diameter = max(diameter, max_diameter)
            # print(diameter)
            
            return 1 + max(left_depth, right_depth)
        dfs(root, 0)
        return max_diameter