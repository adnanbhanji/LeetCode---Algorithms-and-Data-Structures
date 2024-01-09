class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # first find intersection point
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # now we have found an intersection, so move slow back to start and move both by 1 till they're equal at some point.
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast