# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None
        
        prev = None 
        curr = head
        #basically set the pointer of the one in front to the next value 
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp 
        return prev

            

        
