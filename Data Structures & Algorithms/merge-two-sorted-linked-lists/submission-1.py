# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """ 
        compare the values of both list whichever is smallest append to the list move that one forward repeat till both are empty 
        """

        start = ListNode()
        ptr = start
        curr = list1 
        curr2 = list2 
        while curr and curr2: 
            if curr.val < curr2.val: 
                ptr.next = curr
                ptr = ptr.next
                curr = curr.next
            elif curr2.val <= curr.val: 
                ptr.next = curr2
                ptr = ptr.next 
                curr2 = curr2.next 
            
        if not curr and curr2: 
            ptr.next = curr2
        elif not curr2 and curr: 
            ptr.next = curr

        
        return start.next
        