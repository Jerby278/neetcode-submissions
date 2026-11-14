# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        #curr = head
        prev = None
        while head: #reverse them
            holder = head.next # hold the next linked list
            head.next = prev
            prev = head
            head = holder
        return prev