class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_arr = []
        nums = sorted(nums)
        len_nums = len(nums)-1
        for i in range(len_nums):
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    if [nums[i],nums[left],nums[right]] not in final_arr:
                        final_arr.append([nums[i],nums[left],nums[right]])

                    left += 1 
                    right -= 1   
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return final_arr