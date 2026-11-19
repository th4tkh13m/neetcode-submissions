# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = []
        stack.append(root)

        while stack:
            current_node = stack.pop()
            if current_node:

                current_node.left, current_node.right = current_node.right, current_node.left
                stack.append(current_node.left)
                stack.append(current_node.right)
            
        return root

        