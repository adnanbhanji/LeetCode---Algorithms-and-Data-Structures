from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_window = []
        left = 0
        len_nums = len(nums)
        queue = deque()
        for i in range(len_nums):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

            if left > queue[0]:
                queue.popleft()

            if (i+1) >= k:
                max_window.append(nums[queue[0]])
                left += 1

        return max_window