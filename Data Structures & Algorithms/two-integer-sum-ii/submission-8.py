class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """ 
        Solution must be O(1), space - can not save indexes of numbers
        """
        # O(nlogn) -> for sorting
        numbers.sort() 
        # this does not seem efficient so we would go O(n) and then logn for each 
        for i, num in enumerate(numbers): 
            # basically look for the next element above 
            look = target - num  
            #binary serach for look 
            l = i + 1 
            r = len(numbers) - 1
            while l < len(numbers) - 1 and l <= r:
                mid = (l + r) // 2
                print(f"Current Midpoint {mid}")
                if numbers[mid] == look: 
                    return [i + 1, mid + 1]
                #greater than the current value you want to move the right down
                elif numbers[mid] > look: 
                    r = mid - 1 
                else: 
                    l = mid + 1 
            
            

            
            

        
