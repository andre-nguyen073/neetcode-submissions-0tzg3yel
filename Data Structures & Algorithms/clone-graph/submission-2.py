class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return
 
        graph = Node(val=node.val)
        
        visited = {node.val: graph} 
        
        def dfs(current_clone, original_node): 
            for original_neighbor in original_node.neighbors: 
                if original_neighbor.val not in visited: 
                    new_node = Node(val=original_neighbor.val)
                    
                    visited[original_neighbor.val] = new_node
                    
                    current_clone.neighbors.append(new_node)
                    
                    dfs(new_node, original_neighbor)
                    
                else:
                    existing_clone = visited[original_neighbor.val]
                    current_clone.neighbors.append(existing_clone)

        dfs(graph, node)
        return graph