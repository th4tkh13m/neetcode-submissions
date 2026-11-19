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
        
        queue = []
        queue.append(root)

        while queue:
            current_node = queue.pop(0)
            if current_node:

                current_node.left, current_node.right = current_node.right, current_node.left
                queue.append(current_node.left)
                queue.append(current_node.right)
            
        return root

        