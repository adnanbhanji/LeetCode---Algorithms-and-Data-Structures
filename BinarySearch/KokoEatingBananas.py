class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_val = float('inf')

        while left <= right:
            mid = (left+right)//2
            counter = 0
            for i in piles:
                temp = math.ceil(i/mid)
                counter += temp 
            
            if counter <= h:
                min_val = min(min_val, mid)
                right = mid-1
            else:
                left = mid + 1
            
        return min_val


        


                