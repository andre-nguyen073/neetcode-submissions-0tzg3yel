class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ 
        take the string split it up and then join it
        we need to ignore all special characters how?
        """ 
        s.split(" ") 
        string = ""
        for val in s: 
            if val.isalnum(): 
                string += val 
        #two cases if its an odd number or is an even number 
        
        #odd case 
        print(string)
        print(len(string))
        if len(string) % 2 == 1: 
            middle = int(len(string) / 2) 
            left = middle - 1 
            right = middle + 1 
            while left >= 0 and right < len(string): 
                if string[left].upper() != string[right].upper():
                    return False 
                left -= 1 
                right += 1
        
        else: 
            right = int(len(string) / 2)
            left = right - 1 
            while left >= 0 and right < len(string): 
                if string[left].upper() != string[right].upper():
                    return False 
                left -= 1 
                right += 1
        
        return True 
