class Solution:
    def isAnagram(self, s: str, t: str) -> bool:    
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in range(len(t)):
            if t[i] not in t_map:
                t_map[t[i]] = 1
            else:
                t_map[t[i]] += 1

            if s[i] not in s_map:
                s_map[s[i]] = 1
            else:
                s_map[s[i]] += 1

        if s_map == t_map:
            return True
        
        return False