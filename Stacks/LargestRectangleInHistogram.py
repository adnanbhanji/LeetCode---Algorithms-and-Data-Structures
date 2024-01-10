class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # store index, value
        max_area = 0
        for idx, height in enumerate(heights):
            start = idx
            while stack and height < stack[-1][1]:
                pop_idx, pop_height = stack.pop()
                area = (idx - pop_idx) * pop_height
                max_area = max(max_area, area)
                start = pop_idx
            
            stack.append([start, height])
        
        for idx, height in stack:
            area = (len(heights)-idx) * height
            max_area = max(max_area, area)
        
        return max_area