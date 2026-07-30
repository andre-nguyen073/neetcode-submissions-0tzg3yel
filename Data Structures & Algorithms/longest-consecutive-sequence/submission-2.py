class Solution:
    from collections import defaultdict
    def longestConsecutive(self, nums: List[int]) -> int:
        """ 
        if number has already been seen it does not matter
        {2: 3}
        {20: 1}
        {4: 3} 

        {3: 3}

        """ 
        nums = set(nums)
        mp = defaultdict(int)
        res = 0
        for num in nums: 
            if not mp[num]: 
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                #then update the length at m
                mp[num - mp[num - 1]] = mp[num] 
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res
