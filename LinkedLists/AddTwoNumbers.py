# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        while l1 or l2:
            if l1:
                num1 += str(l1.val)
                l1 = l1.next
            if l2:
                num2 += str(l2.val)
                l2 = l2.next

        sum_nums = int(num1[::-1]) + int(num2[::-1])
        sum_nums = str(sum_nums)[::-1]

        new_head = ListNode(0)
        temp = new_head
        for i in range(len(sum_nums)):
            new_node = ListNode(int(sum_nums[i]))
            temp.next = new_node 
            temp = new_node
        
        return new_head.next

