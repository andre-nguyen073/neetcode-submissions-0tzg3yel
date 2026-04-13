class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """ 
        non decreasing not equal to strictly increasing 
        the numbers can be the same
        """

        #binary search on a non decreasing array 

        #nlogn solution 
        #already sorted, have to iterate through array and use binary search to find other number 

        def binary_search(array, search): 
            left = 0 
            right = len(array) - 1
            while left <= right:
                mid = (right + left)//2 
                if array[mid] == search: 
                    return mid
                
                elif array[mid] < search: 
                    left = mid + 1 
                else: 
                    right = mid - 1 
            
            return None

        i = 0 
        while i < len(numbers): 
            looking = target - numbers[i] 
            #you can not possible find past this point
            #stop iterating when you reach a point where the numbers are not equal 
            if i < len(numbers) - 1 and numbers[i + 1] == numbers[i]: 
                i += 1 
            
            #search that part of the array

            found = binary_search(numbers[i+1:], looking)
            if found is not None: 
                return [i + 1, found + 1 + i + 1]

            i += 1 


