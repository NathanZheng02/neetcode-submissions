# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow.val == fast.val:
                return True
        
        return False