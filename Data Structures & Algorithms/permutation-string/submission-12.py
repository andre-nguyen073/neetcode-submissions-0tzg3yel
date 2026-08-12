class Solution:
    from collections import Counter
    from collections import defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """ 
        Sliding Frequency_Map -> of size 3 
        """
        mp = Counter(s1)
        mp2 = defaultdict(int)
        l = 0 
        for r, c in enumerate(s2): 
            length = r - l + 1
            #if the length is the greater than s2 move l over
            
            if length > len(s1): 
                mp2[s2[l]] -= 1
                if mp2[s2[l]] == 0: 
                    del mp2[s2[l]]
                l += 1 

            mp2[c] += 1
            if mp == mp2: 
                return True 
        
        return False


            