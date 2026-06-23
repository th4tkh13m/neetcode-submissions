# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        
        # Do in order traversal
        # Return the k-th element

        in_order_list = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal in_order_list
            in_order_list.append(node.val)
            dfs(node.right)
        dfs(root)
        return in_order_list[k - 1]