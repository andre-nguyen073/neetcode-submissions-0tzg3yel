class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ 
        Theres two cases odd case and even case: 
        even ptr 1 

        """
            
        s = "".join(char for char in s if char.isalnum())
        if not s: 
            return True
        ptr1 = 0 
        ptr2 = len(s) - 1
        print(s)
        while ptr1 != ptr2 or ptr2 > ptr1: 
            print(ptr1)
            print(ptr2)
            if s[ptr1].lower() != s[ptr2].lower():
                return False 
            ptr1 += 1
            ptr2 -= 1

        return True