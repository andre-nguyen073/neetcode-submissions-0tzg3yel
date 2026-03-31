class Solution:
    def climbStairs(self, n: int) -> int:
        hashMap = {}
        def recurse_down(curr): 
            if curr in hashMap: 
                return hashMap[curr]
            if curr < 0: 
                return 0 
            if curr == 1: 
                return 1 
            if curr == 2: 
                return 2
            
            unique = recurse_down(curr - 2) + recurse_down(curr - 1)
            hashMap[curr] = unique
            return unique 

        return recurse_down(n)
            
            
            
