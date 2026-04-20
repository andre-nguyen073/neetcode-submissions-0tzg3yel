# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: 
            return 0
        counter = 0
        result = None
        def recurse(node):
            nonlocal counter, result

            if not node or result is not None: 
                return 0

            recurse(node.left)
            counter += 1 
            if counter == k: 
                result = node.val 
                return 

            recurse(node.right)
        
        recurse(root)
        return result
            


            

            
            
            

            

            


        
        
        