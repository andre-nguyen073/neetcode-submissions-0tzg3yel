# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """ 
        Everytime node iterates down a level, iterate the level and add to that specific list
        """
        res = []

        def iterate_down(root, level): 
            nonlocal res
            #Do not add anything
            if not root: 
                return 

            if len(res) <= level: 
                res.append([])
            
            res[level].append(root.val)

            iterate_down(root.left, level + 1)
            iterate_down(root.right, level + 1)
            
            return 
        
        iterate_down(root, 0)
        return res



            

        