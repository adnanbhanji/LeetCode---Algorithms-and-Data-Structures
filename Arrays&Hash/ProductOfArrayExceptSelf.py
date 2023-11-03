class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length_arr = len(nums)
        left = [1] * length_arr
        right = [1] * length_arr

        left_product = 1
        for i in range(len(nums)):
            left[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(len(nums))[::-1]:
            right[i] = right_product
            right_product *= nums[i]

        for i in range(len(left)):
            nums[i] = left[i] * right[i]

        return nums