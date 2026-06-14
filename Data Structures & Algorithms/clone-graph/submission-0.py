"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Normal idea: Do BFS on starting node
        # Create node when the node is not visted
        # Prob: newly create node != old node => 2 set to track?
        # Hash map: val -> Node
        if not node:
            return None
        
        old_to_clone = {}
        visit = set()
        queue = [node]
        prev = None
        while queue:
            for i in range(len(queue)):
                current = queue.pop(0)
                if current and not current in visit:

                    visit.add(current)
                    if not current in old_to_clone:
                        old_to_clone[current] = Node(val=current.val, neighbors=[])

                    for neighbor in current.neighbors:
                        if not neighbor in visit:
                            queue.append(neighbor)
                        if not neighbor in old_to_clone:
                            old_to_clone[neighbor] = Node(val=neighbor.val, neighbors=[])
                        old_to_clone[current].neighbors.append(old_to_clone[neighbor])
        return old_to_clone[node]
                        

