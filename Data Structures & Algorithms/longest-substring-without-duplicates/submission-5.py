class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 
        for this one using a set is tough, because once you get to a repeating value: 
        you have to delete all values before that value -> how do you know where the cutoff is? 
        abcdba
        set = a b c d -> run into b -> if the pointer is at the beginning we can move left right 2 1 point and remove that value 
        """
        
        l = 0
        r = 0
        longest = 0 
        curr = set() 
        print(s)
        while r < len(s): 
            while s[r] in curr: 
                curr.remove(s[l])
                l += 1
            curr.add(s[r])
            
            if len(curr) > longest: 
                longest = len(curr)
            r += 1
        
        return longest

