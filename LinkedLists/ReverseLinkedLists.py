# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev - None: temp -> next -> next
        prev = None
        temp = head
        while temp is not None:
            next_ = temp.next
            temp.next = prev
            prev = temp
            temp = next_

        return prev
            