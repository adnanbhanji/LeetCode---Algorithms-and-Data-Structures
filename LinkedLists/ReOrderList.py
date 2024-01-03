# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head and head.next:
            return None

        temp = head
        slow = temp
        fast = temp.next #works fine in odd cases even with temp, but for even we get the first even val, compared to second 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        temp = slow.next
        slow.next = None
        # now consider slow = start, fast = end
        while temp is not None:
            _next = temp.next
            temp.next = prev
            prev = temp
            temp = _next
        
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        