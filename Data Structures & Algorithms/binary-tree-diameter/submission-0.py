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
        def findDepthAndLevel(root):
            if not root:
                return  0
            else:
                left_depth = findDepthAndLevel(root.left)
                right_depth = findDepthAndLevel(root.right)
                depth = 1 + max(left_depth, right_depth)
                
            return depth
        max_diameter = 0
        left_depth = findDepthAndLevel(root.left)
        right_depth = findDepthAndLevel(root.right)
        diameter = left_depth + right_depth
        return max(diameter, max_diameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        

