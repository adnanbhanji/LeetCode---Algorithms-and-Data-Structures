class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        
        max_water = 0

        while left < right:
            val_left = height[left]
            val_right = height[right]
            min_val = min(val_left, val_right)

            max_water = max(max_water, min_val*(right-left))

            if min_val == val_left:
                left += 1
            else:
                right -= 1
        
        return max_water


            


        