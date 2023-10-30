class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_nums = {}
        for i in range(len(nums)):
            if ( target - nums[i]) in store_nums:
                return [i, store_nums[target-nums[i]]]
            else:
                store_nums[nums[i]] = i