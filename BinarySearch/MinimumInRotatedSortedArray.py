class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        min_val = float(inf)

        while left<=right:
            mid = (left+right)//2
            if nums[mid] < min_val:
                min_val = nums[mid]

            if nums[left] <= nums[mid] and nums[right] <= nums[mid]: #we know its been rotated
                left = mid + 1
            else:
                right = mid-1
        
        return min_val
