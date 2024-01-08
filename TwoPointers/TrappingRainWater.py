class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        water = 0
        max_left = height[0]
        max_right = height[-1]
        left_ptr = 0
        len_height = len(height) 
        right_ptr = len_height-1

        while left_ptr < right_ptr:
            if max_left < max_right:
                left_ptr += 1
                max_left = max(max_left, height[left_ptr])
                water += max_left - height[left_ptr]
            else:
                right_ptr -= 1
                max_right = max(max_right, height[right_ptr])
                water += max_right - height[right_ptr]
        
        return water