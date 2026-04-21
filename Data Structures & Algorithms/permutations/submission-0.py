class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        """ 
        Is there a better way to just skip indexes we already visited besides keeping track?

        """
        def permutation(curr, seen): 
            nonlocal res
            if len(curr) == len(nums): 
                res.append(curr)
            
            for i in range(len(nums)): 
                if i not in seen:
                    temp = seen.copy()
                    temp.add(i)
                    permutation(curr + [nums[i]], temp)
                    

        permutation([], set())
        return res 




        
