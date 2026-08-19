# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ 
        removing the nth node from the end what does that involve - end node - n = node to remove right 
        what if we just iterate over it and keep track of every node in a hashmap and then go to that exact node when we are done 
        """ 
        if not head: 
            return None

        #what if we lag a pointer n away 
        ptr1 = head 
        cnt = 0
        ptr2 = head 

        while ptr2.next:
            if cnt != n: 
                cnt += 1 
            else: 
                ptr1 = ptr1.next

            ptr2 = ptr2.next 
        
        #what happens if theres is nothing in front that would only happen in 0 case right
        if not ptr1.next: 
            ptr1.next = None
        else:
            ptr1.next = ptr1.next.next
        #also there is a case where it is the first node
        if ptr1 == head:
            return head.next

        return head

            
        

        
        







