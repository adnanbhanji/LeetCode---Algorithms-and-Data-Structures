# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # so let's try with slow and fast to get O(n) on avg
        if not head:
            return None

        new_node = ListNode(0, head)
        slow = new_node
        fast = head

        for i in range(n):
            fast = fast.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return new_node.next
