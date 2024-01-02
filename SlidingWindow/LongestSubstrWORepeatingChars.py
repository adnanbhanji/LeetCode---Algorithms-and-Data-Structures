class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        encountered = {}
        anchor = 0 
        len_s = len(s)
        max_substr = 0
        for i in range(len_s):
            if s[i] in encountered and encountered[s[i]] >= anchor:
                anchor = encountered[s[i]]+1
            
            max_substr = max(max_substr, i-anchor+1)
            encountered[s[i]] = i

        return max_substr
                