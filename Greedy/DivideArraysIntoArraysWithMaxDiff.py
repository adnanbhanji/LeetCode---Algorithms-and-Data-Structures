class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        final = []
        temp = []
        for i in range(len(nums)):
            if len(temp) < 3:
                temp.append(nums[i])
                if i == len(nums)-1:
                    final.append(temp)
            else:
                final.append(temp)
                temp = []
                temp.append(nums[i])

            if temp[-1] - temp[0] > k:
                return []
        
        return final
                
        