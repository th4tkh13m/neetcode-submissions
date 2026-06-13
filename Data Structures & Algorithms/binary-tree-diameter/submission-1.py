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
        self.res = 0
        def findDepthAndLevel(root):
            if not root:
                return  0
            else:
                left_depth = findDepthAndLevel(root.left)
                right_depth = findDepthAndLevel(root.right)
                self.res = max(self.res, left_depth + right_depth)
                depth = 1 + max(left_depth, right_depth)
                
            return depth
        findDepthAndLevel(root)
        return self.res
        

