class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #the tree is symmetrical 
        def invert(root): 
            if not root: 
                return None 
            
            left = invert(root.left)
            right = invert(root.right)
            

            root.left = right 
            root.right = left 

            return root

        invert(root)
        return root
            

