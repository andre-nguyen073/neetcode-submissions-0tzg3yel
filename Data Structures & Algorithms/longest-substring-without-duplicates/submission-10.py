class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 
        longest substring without duplicates - basically keep track of when dup
        is the longest?
        """

        """ 
        what about hashmap 
        if key is in hashmap s
        """
        mp = {} 
        max_len = 0
        for i, char in enumerate(s):
            if char not in mp: 
                mp[char] = i 
                if len(mp) > max_len: 
                    max_len = len(mp)
            else: 
                j = i - 1 
                while j >= 0 and s[j] in mp: 
                    mp.pop(s[j])
                    j -= 1 
                mp[char] = i 

        return max_len



        

