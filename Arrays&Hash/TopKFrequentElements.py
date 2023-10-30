class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store_frequent = {}

        for i in range(len(nums)):
            if nums[i] in store_frequent:
                store_frequent[nums[i]] += 1
            else:
                store_frequent[nums[i]] = 1
        
        sorted_elements = sorted(store_frequent.items(), key=lambda x: x[1], reverse=True)
        sorted_keys = [element[0] for element in sorted_elements[:k]]
        return sorted_keys