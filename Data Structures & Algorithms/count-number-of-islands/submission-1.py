class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """ 
        Once you find one island iterate around it, looking for another connected piece. 
        """
        #iterate over the grid - whenever you see a node you already visited skip - if it starts with a 1 unvisited then dfs count that as a island 
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
        visited = set()
        #explore all the values that are reachable - mark them as visited 
        def dfs(x, y): 
            visited.add((x,y))

            for dx, dy in directions: 
                nx = dx + x 
                ny = dy + y 
                #within the bounds
                if (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) and grid[nx][ny] == "1" and (nx,ny) not in visited:
                    dfs(nx,ny) 


            



        res = 0 
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if (i,j) not in visited and grid[i][j] == "1": 
                    dfs(i,j)
                    res += 1
        
        return res
        