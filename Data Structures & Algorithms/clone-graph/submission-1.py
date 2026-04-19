"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return
        graph = Node(val=node.val)
        visited = set()
        def dfs(current, node): 
            visited.add(node.val)
            print(f"What we have visited so far: {visited}")
            neighbors = node.neighbors
            for neighbor in neighbors: 
                if neighbor.val not in visited: 
                    new_node = Node(val=neighbor.val)
                    #undirected has to go back and forth
                    new_node.neighbors.append(current)
                    current.neighbors.append(new_node)
                    dfs(new_node, neighbor)

        dfs(graph, node)
        return graph



            

