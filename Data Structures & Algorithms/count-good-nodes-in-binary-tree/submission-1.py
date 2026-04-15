# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """ 
        Keep track of the last good node in the paths value, aka highest value 
        if that nodes value is < than the current value then you can add 1 
        """
        good_nodes = 0 
        if not root: 
            return 0

        """
        returns the total number of good nodes the this section
        """ 
        """ 
        dfs(2, 2) -> dfs(1, 2) -> dfs(5, Null) 
                                ->     0


        """
        def dfs(node, largest):
            if not node: 
                return 0 

            #then we want to return one right 
            if node.val >= largest: 
                return dfs(node.left, node.val) + dfs(node.right, node.val) + 1
            else: 
                return dfs(node.left, largest) + dfs(node.right, largest) 
            
            
        #adds 1 for the starting node
        return dfs(root, root.val)
        