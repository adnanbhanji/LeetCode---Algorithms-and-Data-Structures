class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_word = ""
        max_length = max(len(word1),len(word2))
        for i in range(max_length):
            if i < len(word1):
                final_word += word1[i]
            if i < len(word2):
                final_word += word2[i]
        return final_word
        