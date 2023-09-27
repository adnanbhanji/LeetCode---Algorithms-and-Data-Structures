class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        left=0 
        while left < len(chars):
            right = left
            while right < len(chars) and chars[left] == chars[right]:
                right += 1
            
            chars[index] = chars[left]
            index += 1
            
            value = right - left
            
            if value >= 2:
                for i in list(str(value)):
                    chars[index] = i
                    index += 1
                    
            left = right 
            
        return index
                
            