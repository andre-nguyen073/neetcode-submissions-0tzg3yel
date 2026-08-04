class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #area is just the heighest bars together 
        l = 0 
        r = len(heights) - 1 

        """ 
        How do we know when to iterate left or right? 
        Always keep the higher move the smaller one 
        - Why you always want the highest bars 
        """
        highest_area = 0
        while l < r: 
            #need the width for area
            min_heights = min(heights[l], heights[r])
            curr_area = min_heights * (r - l)
            if curr_area > highest_area: 
                highest_area = curr_area
            if heights[l] < heights[r]: 
                #move the left up 
                l += 1 
            else: 
                r -= 1 
        
        return highest_area

            
