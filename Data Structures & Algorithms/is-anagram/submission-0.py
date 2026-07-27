class Solution:
    from collections import defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        """ 
        First thoughts get frequency maps for each if they match then its the same?
        """
        frequency_map = defaultdict(int)
        for char in s: 
            frequency_map[char] += 1 
        
        for char in t: 
            if char in frequency_map:
                frequency_map[char] -= 1 
                if frequency_map[char] < 0: 
                    return False
            else: 
                return False

        return True
            