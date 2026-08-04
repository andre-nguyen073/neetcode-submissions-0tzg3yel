class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 
        longest substring without duplicates - basically keep track of when dup
        is the longest?
        """

        """ 
        xyzzy

        """
        max_set = 0
        dup = set()
        for char in s: 
            if char not in dup: 
                dup.add(char)
                if len(dup) > max_set: 
                    max_set = len(dup)
            else: 
                dup = set()
                dup.add(char)
        
        return max_set

