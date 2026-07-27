class Solution:
    from collections import Counter
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """ 
        really the main issue is how do we query the different frequency_maps 
        So we will have mutiple frequency_maps which link to mutiple different strings 
        dictionary concsisting of dictionary and array return all the arrays

        """
        seen = defaultdict(list)
        #issue is this is O(n^2) process since converting every one of these to dictionary cost O(N)
        for string in strs: 
            sorted_string = "".join(sorted(string))
            seen[sorted_string].append(string)
        
        return list(seen.values())

                
            

            
            
