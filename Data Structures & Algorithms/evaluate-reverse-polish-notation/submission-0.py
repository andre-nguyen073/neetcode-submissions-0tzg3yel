class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """ 
        treat Tokens as a stack
        reverse and then pop items accordingly, 
        """
        if not tokens:
            return 0
        num1 = None
        num2 = None
        stack = list(reversed(tokens))
        while stack: 
            curr = stack.pop()
            print(curr)
            if curr == '+': 
                num1 += num2 
            elif curr == '*':
                num1 *= num2 
            elif curr == '/': 
                num1 = num1/num2
            elif curr == '-': 
                num1 -= num2
            else:
                curr = int(curr)
            if not num1:
                num1 = curr
            else: 
                num2 = curr
        

        return num1

