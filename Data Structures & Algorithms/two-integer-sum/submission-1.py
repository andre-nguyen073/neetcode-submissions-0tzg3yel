class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums): 
            looking_for = target - num
            if looking_for in seen: 
                return [seen[looking_for], i]
            else: 
                seen[num] = i
        
            
