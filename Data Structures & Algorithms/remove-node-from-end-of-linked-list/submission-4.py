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

        mp = {}
        cnt = 0
        curr = head 
        while curr: 
            cnt += 1
            print(cnt)
            mp[cnt] = curr
            print(mp)
            curr = curr.next
        
        #when your at the end curr is done 
        #node to remove 
        #long edge case is if its the first node 
        node_to_remove = cnt - n + 1
        #if its the first node 
        if node_to_remove == 1: 
            head = head.next 
            return head 
        else: 
            prev = mp[node_to_remove - 1]
            prev.next = mp[node_to_remove].next
        
        return head
        

        
        







