class Solution:
    def isValid(self, s: str) -> bool:
        """ 
        Why is stack used - stack is first in first out, so if you put in a parenthesis, you need to pop that out, aka if you did [(, youd need a ) to match, same principle applies to parenthesis
        """
        stack = []
        for char in s: 
            if char == '(' or char == '[' or char == '{': 
                stack.append(char) 
            elif not stack: 
                return False 
            else: 
                curr = stack.pop()
                if (char == ']' and curr != '[') or (char == '}' and curr  != '{') or (char == ')' and curr != '('): 
                    return False 
        return True