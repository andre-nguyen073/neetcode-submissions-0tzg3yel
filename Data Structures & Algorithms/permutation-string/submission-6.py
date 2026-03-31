class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashMap1 = defaultdict(int)
        for char in s1: 
            hashMap1[char] += 1

        if len(s2) < len(s1):
            return False
        
        i = 0 
        x = 0
        hashMap2 = defaultdict(int)
        while i < len(s2): 
            if i > len(s1) - 1:
                hashMap2[s2[x]] -= 1
                if hashMap2[s2[x]] == 0: 
                    hashMap2.pop(s2[x])
                x += 1 

            hashMap2[s2[i]] += 1
            print(hashMap2)
            if hashMap1 == hashMap2:
                return True
             
            i += 1
        return False
            
            
            
            
        

        