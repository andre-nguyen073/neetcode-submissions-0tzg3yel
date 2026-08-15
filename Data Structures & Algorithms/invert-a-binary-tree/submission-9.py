class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ 
        iterate over left and right seperately, switch values 
        binary tree so theres always a value on both sides
        """
        
        if not root: 
            return None
        def dfs(r1, r2):
            if not r1 or not r2: 
                return 
            temp = r1.val 
            r1.val = r2.val 
            r2.val = temp 
            #search both sides performing the swaps. 
            dfs(r1.left, r2.right)
            dfs(r1.right, r2.left)
            
        dfs(root.left, root.right)
        return root
            

