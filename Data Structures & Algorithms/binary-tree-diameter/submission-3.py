# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #you want to get the max depth of left and right and add them together
        #but you have to compare that max_depth the depth of the local max
        res = 0
        def max_depth(root): 
            nonlocal res
            if not root: 
                return 0 
            left_height = max_depth(root.left)
            right_height = max_depth(root.right)

            depth = left_height + right_height 
            if depth > res: 
                res = depth 
            
            return 1 + max(left_height, right_height)
        max_depth(root)
        return res
            


            
            
            
        

            
            
