"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Idea: create a hashmap map: old node -> new node
        # Create new node while traverse and create adj list
        # Do BFS
        if not node:
            return None

        node_map = {}
        visit = set()
        queue = [node]

        visit.add(node)

        while queue:
            for i in range(len(queue)):
                current_node = queue.pop(0)
                if current_node:
                    if not current_node in node_map:
                        node_map[current_node] = Node(val=current_node.val, neighbors=[])
                    
                    for neighbor in current_node.neighbors:
                        if not neighbor in visit:
                            queue.append(neighbor)
                            visit.add(neighbor)

                        if not neighbor in node_map:
                            node_map[neighbor] = Node(val=neighbor.val, neighbors=[])
                        
                        node_map[current_node].neighbors.append(node_map[neighbor])
        return node_map[node]







        