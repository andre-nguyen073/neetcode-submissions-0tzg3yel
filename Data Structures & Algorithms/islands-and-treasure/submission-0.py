class Solution:
    from collections import deque
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """ 
        multi step bfs
        """
        queue = deque()
        for r in range(len(grid)): 
            for c in range(len(grid[0])): 
                if grid[r][c] == 0: 
                    queue.append((r,c, 0))

        directions = [
            (1,0), 
            (-1,0), 
            (0,1), 
            (0,-1)
        ]

        #how do you keep track at what level you are at
        #how do we ensure we do not explore the same values again
        while queue: 
            r, c, l = queue.popleft()
            #three cases inf, 0, or -1 
            for dx, dy in directions: 
                horizontal = r + dx 
                vertical = c + dy
                if 0 <= horizontal < len(grid) and 0 <= vertical < len(grid[0]):
                    if grid[horizontal][vertical] == 2147483647:
                        grid[horizontal][vertical] = l + 1
                        queue.append((horizontal, vertical, l + 1))





                    
            




        

        

