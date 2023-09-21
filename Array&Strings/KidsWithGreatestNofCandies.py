class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        length = len(candies)
        result = []
        for i in range(length):
            temp = candies[i] 
            extra = candies[i] + extraCandies
            candies[i] = extra
            max_val = max(candies)
            if extra == max_val: 
                result.append(True)
            else:
                result.append(False)
            candies[i] = temp
        return result

