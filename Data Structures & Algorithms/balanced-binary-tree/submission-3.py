# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #perform bfs on left and right - keep track of max height - if height > 1 than return False 
        if not root: 
            return True
        
        def get_height(root): 
            if not root: 
                return 0 
            
            height = max(get_height(root.left), get_height(root.right)) + 1 
            return height
            

            


        h_left = get_height(root.left)
        h_right = get_height(root.right)
        if max(h_left, h_right) - min(h_left, h_right) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

            