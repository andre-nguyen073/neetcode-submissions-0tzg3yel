# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #level order traversal but always return the ones on the right 
        res = []
        temp = []
        def recursive_sol(root, level): 
            nonlocal temp
            if not root: 
                return

            if len(temp) == level: 
                temp.append([])
            
            temp[level].append(root.val)

            recursive_sol(root.left, level + 1)
            recursive_sol(root.right, level + 1)

        recursive_sol(root, 0)
        for array in temp: 
            res.append(array[-1]) 

        return res
            
            

        

        