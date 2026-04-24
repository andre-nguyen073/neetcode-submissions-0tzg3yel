# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(t1, t2, checking): 
            #final condiiton if you get to the bottom of both without any issues return True
            if (not t1 and not t2) and checking:
                print("this runs for sure")
                return True 
            elif (not t1 and not t2) and not checking: 
                return False
            elif (not t1 and t2) or (not t2 and t1): 
                return False 
            
            #Start checking subtree in iteration
            if t1.val == subRoot.val: 
                return dfs(t1.left, t2.left, True) and dfs(t1.right, t2.right, True)
            
            if not checking or (checking and t1.val != t2.val): 
                return dfs(t1.left, subRoot, False) and dfs(t1.right, subRoot, False)
        
        return dfs(root, subRoot, False)

            
        
        
            


            



