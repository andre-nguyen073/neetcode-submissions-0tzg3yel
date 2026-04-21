class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        """ 
        Is there a better way to just skip indexes we already visited besides keeping track?
        """
        #whole concept of backtracking is removing the last decision
        def permutation(curr): 
            nonlocal res
            if len(curr) == len(nums): 
                res.append(curr.copy())
                return
            
            for i in range(len(nums)): 
                if i not in seen:
                    seen.add(i)
                    curr.append(nums[i])
                    permutation(curr)
                    curr.pop()
                    seen.remove(i)

                
        permutation([])
        return res 




        
