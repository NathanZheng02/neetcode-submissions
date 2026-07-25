# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        # Get the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        sec_half = slow.next
        # Split halves
        slow.next = None
        prev = None

        while sec_half:
            temp = sec_half.next
            sec_half.next = prev
            prev = sec_half
            sec_half = temp

        # Merge
        first = head
        second = prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

