class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        strList = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            while left < right and strList[left] not in vowels:
                left += 1
            while left < right and strList[right] not in vowels:
                right -= 1
            strList[left], strList[right] = strList[right], strList[left]
            left += 1
            right -= 1
        final_str = "".join(strList)
        return final_str