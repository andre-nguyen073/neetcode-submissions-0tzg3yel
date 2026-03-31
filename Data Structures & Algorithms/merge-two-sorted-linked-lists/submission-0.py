class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        res = ListNode()
        final = res 
        if list1 and not list2: 
            return list1 

        if list2 and not list1: 
            return list2  
        
        while list1 and list2: 
            if list1.val <= list2.val: 
                res.next = list1
                list1 = list1.next 
            else: 
                res.next = list2
                list2 = list2.next 
                
            res = res.next
        
        if not list1: 
            res.next = list2
        elif not list2: 
            res.next = list1
        
        return final.next