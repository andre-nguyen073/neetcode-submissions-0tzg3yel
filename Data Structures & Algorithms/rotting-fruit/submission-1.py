class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """ 
        0 is emptyt 
        1 is fruit 
        2 is a rotten fruit 
        first iteate over to find all the rotten fruit 
        perform bfs on each fruit adding the next fruit to the queue 
        you can just return the level of the last fruit.

        how do we check that all fruit are rotten? 
        keep counter of rotten fruit does not match total, then return -1. 
        """
        directions = [
            (1,0),
            (-1,0), 
            (0,1), 
            (0,-1)
        ]
        queue = deque()
        total_fruit = 0
        for r in range(len(grid)): 
            for c in range(len(grid[0])): 
                #the fruit is rotten or fresh
                if grid[r][c] == 2 or grid[r][c] == 1: 
                    total_fruit += 1
                if grid[r][c] == 2: 
                    queue.append((r,c,0))
        
        #Right now the queue contains all the rotten fruit in the form 
        #ROW, COLUMN, LEVEL 
        rotten_fruit = 0
        max_level = 0
        while queue: 
            row, column, level = queue.popleft()
            if level > max_level: 
                max_level = level
            rotten_fruit += 1
            for dx,dy in directions: 
                horizontal = row + dx 
                vertical = column + dy 
                #check to see if there is a fresh fruit 
                if 0 <= horizontal < len(grid) and 0 <= vertical < len(grid[0]): 
                    if grid[horizontal][vertical] == 1: 
                        #set to rotten so it does not get added to queue 
                        grid[horizontal][vertical] = 2 
                        queue.append((horizontal, vertical, level + 1))
        
        if rotten_fruit != total_fruit: 
            return -1 
        
        return max_level


                


        