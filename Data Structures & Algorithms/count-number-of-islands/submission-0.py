class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """ 
        Once you find one island iterate around it, looking for another connected piece. 
        """
        def breath_first_search(i,j):
            #check up, check down, check left, check right 
            #check right
            if i + 1 < len(grid) and grid[i + 1][j] == "1" and (i + 1, j) not in seen:
                seen.add((i + 1, j))
                breath_first_search(i + 1, j)

            if i - 1 >= 0 and grid[i - 1][j] == "1" and (i - 1, j) not in seen:
                seen.add((i - 1, j))
                breath_first_search(i - 1, j)

            if j + 1 < len(grid[0]) and grid[i][j+ 1] == "1" and (i, j + 1) not in seen:  
                seen.add((i, j + 1))
                breath_first_search(i, j + 1)

            if j - 1 >= 0 and grid[i][j - 1] == "1" and (i, j - 1) not in seen:
                seen.add((i, j - 1))
                breath_first_search(i, j - 1)
            return
        
        seen = set()
        counter = 0 
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] == "1" and (i,j) not in seen: 
                    seen.add((i,j))
                    counter += 1 
                    breath_first_search(i,j) 
        

    

        return counter 

