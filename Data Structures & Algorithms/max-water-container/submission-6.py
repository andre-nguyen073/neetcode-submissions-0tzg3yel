class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """ 
        ahhh, something I never thought about is that you always want the highest line, if any line is shorter than the highest, you 
        can move the other pointer 
        """

        left = 0 
        right = len(heights) - 1
        res = 0
        while left < right: 
            area = min(heights[left], heights[right])  * (right - left)
            res = max(area, res)
            if heights[left] <= heights[right]: 
                left += 1
            else: 
                right -= 1
        
        return res