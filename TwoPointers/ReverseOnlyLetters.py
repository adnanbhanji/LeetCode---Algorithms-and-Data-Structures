class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # "a-bC-dEf-ghIj"
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        strLst = list(s)
        left = 0
        right = len(strLst) - 1
        while left < right:
            while left < right and strLst[left] not in letters:
                left += 1
            while left < right and strLst[right] not in letters:
                right -= 1
            
            strLst[left], strLst[right] = strLst[right], strLst[left]

            left += 1
            right -= 1

        return "".join(strLst)
