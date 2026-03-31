# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def check_balance(root): 
            nonlocal res

            if not root: 
                return 0

            left = check_balance(root.left)
            right = check_balance(root.right)

            if abs(right - left) > 1: 
                res = False 
            
            return 1 + max(left, right)

        check_balance(root)
        return res
            