class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        store = {}
        max_freq = 0
        for i in range(len(s)):
            if s[i] not in store:
                store[s[i]] = 1
            else:
                store[s[i]] += 1

            max_freq = max(max_freq, store[s[i]])

            while (i - left + 1) - max_freq > k:
                store[s[left]] -= 1
                left += 1
            
            longest = max(longest, i-left+1)
        
        return longest