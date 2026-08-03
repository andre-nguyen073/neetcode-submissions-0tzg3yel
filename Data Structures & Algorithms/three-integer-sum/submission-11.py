class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ 
        key thoughts to note: 
        sets are completely useless -> can have mutiple elements different indexes
        Solution: 
        Iterate over array: 
            take curr element: 
            start j at i + 1
            start k at len(nums) - 1
            add total sum if sum is too small iterate j forwards, else k backwards
        
        """
        if not nums: 
            return []
        #run time is (nlogn^2) -> sorting then iterate over all elements per element
        nums.sort()
        #can be mutiple numbers
        res = []
        for i, num in enumerate(nums): 
            if i > 0 and num == nums[i - 1]:
                continue
            j = i + 1 
            k = len(nums) - 1
            #you can not have a triplet at the second to last element 
            if i == len(nums) - 2: 
                break
            # iterate until they cross
            while j < k: 
                sum = num + nums[j] + nums[k]
                #sum is too large move right pointer down
                if sum > 0: 
                    k = k - 1 
                #sum is too small move left pointer up
                elif sum < 0: 
                    j = j + 1 
                #equals 0 this solution works!
                else: 
                    res.append([num, nums[j] ,nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1


        return res
                
