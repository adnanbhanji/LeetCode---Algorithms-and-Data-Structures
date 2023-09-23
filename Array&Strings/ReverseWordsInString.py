class Solution:
    def reverseWords(self, s: str) -> str:
        s_new = s.split(' ')
        new_words = []
        for i in range(len(s_new)):
            s_new[i] = s_new[i].split()
            for j in s_new[i]:
                j.replace(' ', '')  
                new_words.append(j)
        return " ".join(new_words[::-1])
            