class Solution:
    from collections import defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        """ 
        First thoughts get frequency maps for each if they match then its the same?
        """

        frequency_map = defaultdict(int)
        longer_string = None
        shorter_string = None
        if len(s) > len(t): 
            longer_string = s
            shorter_string = t
        else: 
            longer_string = t
            shorter_string = s

        for char in shorter_string: 
            frequency_map[char] += 1 
        print(frequency_map)
        
        for char in longer_string: 
            if char in frequency_map:
                frequency_map[char] -= 1 
                if frequency_map[char] < 0: 
                    return False
            else: 
                return False

        return True
            