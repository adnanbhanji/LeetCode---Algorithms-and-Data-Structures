class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallestnum, secondsmallestnum = float(inf), float(inf)
        for i in nums:
            if i <= smallestnum:
                smallestnum = i
            elif i <= secondsmallestnum:
                secondsmallestnum = i
            else:
                return True
        return False