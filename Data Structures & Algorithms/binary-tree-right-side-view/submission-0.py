# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        i = 0
        while queue:
            # print(i, queue)
            # Right side node:
            right_node = queue[-1]
            res.append(right_node.val)
            for i in range(len(queue)):
                # To traverse
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res