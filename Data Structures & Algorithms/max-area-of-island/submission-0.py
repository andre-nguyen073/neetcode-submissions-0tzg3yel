class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """ 
        iterate over the graph until you find a grid with value of 1
        depth_first_search solution 
        question? 
        What do you do when you encounter a value you have already seen, do you skip? 
        1. keep track of an explored set -> O(n) space 
        """
        explored = set() 

        directions = [
            #right 
            (1, 0),
            #left 
            (-1, 0), 
            #up 
            (0 , 1), 
            #down
            (0, -1)
        ]
        #issue of this solution is that it may iterate over values an extra time. 
        max_area = 0
        def dfs(r, c): 
            if (r < 0 or r >= len(grid) or 
                c < 0 or c >= len(grid[0]) or 
                grid[r][c] == 0 or 
                (r, c) in explored): 
                return 0

            total_area = 0
            explored.add((r,c))

            for dx, dy in directions: 
                horizontal = r + dx 
                vertical = c + dy
                total_area = total_area + 1 + dfs(horizontal, vertical)
            
            return total_area

        for r in range(len(grid)): 
            for c in range(len(grid[0])):
                if (r,c) not in explored and grid[r][c] == 1: 
                    local = dfs(r, c)
                    if local > max_area: 
                        max_area = local
                    
        return max_area


        