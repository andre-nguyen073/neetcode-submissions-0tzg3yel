class Solution:
    from collections import defaultdict
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Biggest takeaway from this is the following: 
        Window Length - most_frequent_element -> tells you the amount of replacements you have to do
        if its greater than what you can possible to decrease the window - move left and check again?

        AAABA BBBBBB 
        """

        mp = defaultdict(int)
        l = 0 
        res = 0
        max_f = 0
        for r in range(len(s)): 
            mp[s[r]] += 1
            max_f = max(max_f, mp[s[r]])
            #how do you keep track of most frequenet element
            while (r - l + 1) - max_f > k: 
                mp[s[l]] -= 1 
                l += 1  
            
            res = max(res, r - l + 1)
        
        return res
            
