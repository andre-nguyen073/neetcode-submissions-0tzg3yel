class Solution:

    def encode(self, strs: List[str]) -> str:
        #add a delminator between each value 
        full_string = ""
        for string in strs:
            full_string += f"{len(string)}#{string}"
        print(full_string)
        return full_string


        
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s): 
            j = i  
            # j is the values up to the delminator
            while j < len(s) and s[j] != '#': 
                j += 1 
            length = int(s[i:j])

            start_string = j + 1 
            string_end = start_string + length 
            result.append(s[start_string: string_end])

            i = string_end
        return result
            
            

