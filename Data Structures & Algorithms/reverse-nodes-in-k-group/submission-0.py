# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start = dummy

        while True:
            k_node = self.get_k(start, k)
            # Last Group
            if not k_node:
                break
            
            # The end is set to the start of the next group
            end = k_node.next

            # Reverse
            prev, curr = k_node.next, start.next
            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Resetting pointers so that start is 1 before the group
            # and start.next is starting node of the next group
            temp = start.next
            start.next = k_node
            start = temp
        
        return dummy.next
    
    # Helper function to get k-group
    def get_k(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    