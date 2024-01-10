class Solution:
    def helper_function(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1 
        return True


    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        counter = 0
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            
            else:
                # we could have to delete one char or its false 
                # so we have to check both 
                
                # let's start with moving the left ptr in front
                l = self.helper_function(s, left + 1, right)
                # if left doesn't work we can try with right
                r = self.helper_function(s, left, right-1)
                
                if l or r:
                    return True
                
                if not l and not r:
                    return False
        
        return True

                
                # lets call both 
                

