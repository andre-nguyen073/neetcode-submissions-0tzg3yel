# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ 
        1 -> 2 -> 3 -> 4 -> 5 -> 6
        """
        if not head: 
            return None 
        current = head
        reverse = None
        ptr1 = head 
        ptr2 = head 
        counter = 0

        while ptr2: 
            print("ptr1 value", ptr1.val)
            print("ptr2 value", ptr2.val)
            if counter == n: 
                reverse = ptr1
                ptr1 = ptr1.next 
            
            if counter != n: 
                counter += 1 
            
            ptr2 = ptr2.next
            
        if reverse:
            reverse.next = ptr1.next
        else: 
            head = head.next

        return head






