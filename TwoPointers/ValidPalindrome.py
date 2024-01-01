class Solution:
    def isPalindrome(self, s: str) -> bool:
        # sol 1 - simple arr

        # s = s.lower()
        # final_s = [char for char in s if char.isnumeric() or char.isalpha()]
        # return True if final_s == final_s[::-1] else False
        

        # sol 2 - pointers w nested while 

        # left = 0
        # right = len(s) - 1
        # s = s.lower()
        # while left < right:
        #     while left < right and not (s[left].isnumeric() or s[left].isalpha()):
        #         left += 1
            
        #     while left < right and not (s[right].isnumeric() or s[right].isalpha()):
        #         right -= 1
            
        #     if s[left] != s[right]:
        #         return False
        
        #     left += 1
        #     right -= 1 

        # return True
            
        
        # sol 3 - pointers w if 
        left = 0 
        right = len(s) - 1
        s = s.lower()

        while left < right:
            if (s[left].isnumeric() or s[left].isalpha()) and (s[right].isnumeric() or s[right].isalpha()):
                if s[left] != s[right]:
                    return False
                
                right -= 1
                left += 1

            else:
                if not (s[left].isnumeric() or s[left].isalpha()):
                    left += 1
                if not (s[right].isnumeric() or s[right].isalpha()):
                    right -=1
                    
        return True
            