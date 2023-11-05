class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        left = 0 
        len_chars = len(chars)
        while left < len_chars:
            right = left

            while right < len_chars and chars[left]==chars[right]:
                right += 1
            
            chars[index] = chars[left]
            index += 1

            value = right - left

            if value >= 2:
                for i in list(str(value)):
                    chars[index] = i
                    index += 1
            
            left = right 
        
        return len(chars[:index])

