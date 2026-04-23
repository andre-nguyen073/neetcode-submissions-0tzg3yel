class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dfs(r, c): 
            #you know you made it to the bottom right
            if r == m - 1 and c == n - 1: 
                return 1 
            #you went out of bounds
            if r > m - 1 or c > n - 1: 
                return 0
            
            #else explore 
            return dfs(r + 1, c) + dfs(r, c + 1)


        return dfs(0,0)
        