# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Merge Sort: O(nlog(k))

        # Edge Cases
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged = []

            # Looking at 2 lists at a time to merge
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.merge_list(l1, l2))
            
            # Copy over
            lists = merged

        return lists[0]
    
    # Merging 2 lists code (* Memorize *)
    def merge_list(self, list1, list2):
            # Merge list code
            dummy = ListNode()
            curr = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            
            if list1:
                curr.next = list1
            if list2:
                curr.next = list2
                
            return dummy.next
