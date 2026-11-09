# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head.next
        prev = head
        prev.next = None
        while curr: #reverse them
            holder = curr.next # hold the next linked list
            curr.next = prev
            prev = curr
            curr = holder
        return prev
            
            

        

        


# [0,1,2,3]