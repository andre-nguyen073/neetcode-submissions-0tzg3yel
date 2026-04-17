# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """ 
        iterate over at the same time 
        carry_over
        assume LLs sizes do not have to be the same 
        """
        carry_over = 0
        l3 = ListNode(val=None, next=None)
        current = l3
        while l1 and l2:
            print("L1 Value", l1.val)
            print("L2 Value", l2.val)
            total = 0
            if carry_over == 0:
                total = l1.val + l2.val 
            else: 
                total = l1.val + l2.val + 1
            print("Total", total)
            if total > 9: 
                carry_over = 1
            else: 
                carry_over = 0
            new_node = ListNode(val=total % 10, next=None)
            current.next = new_node 
            current = current.next
            l1 = l1.next 
            l2 = l2.next
        
        #one list is done but the other isnt 
        finish = None 
        if not l1 and l2: 
            finish = l2 
        elif not l2 and l1: 
            finish = l1 

        while finish: 
            total = 0
            if carry_over == 1: 
                total = finish.val + 1
            else: 
                total = finish.val
            
            if total > 9: 
                carry_over = 1
            else: 
                carry_over = 0

            new_node = ListNode(val=total % 10, next=None)
            current.next = new_node
            current = current.next
            finish = finish.next

        if carry_over == 1: 
            new_node = ListNode(val=1, next=None)
            current.next = new_node 

        return l3.next
                
                    

            

             


        
        