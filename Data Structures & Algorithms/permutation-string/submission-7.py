class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding hashmap on s2 
        if len(s2) < len(s1): 
            return False
        mp1 = Counter(s1)
        mp2 = {}
        l = 0
        #just check to see if the frequency_maps are the same 
        for char in s2: 
            mp2[char] = mp2.get(char, 0) + 1
            if sum(mp2.values()) > len(s1): 
                mp2[s2[l]] -= 1 
                if not mp2[s2[l]]: 
                    mp2.pop(s2[l])
                l += 1
            
            if mp2 == mp1: 
                return True 
            
        
        return False
            
            
            
            
        

        